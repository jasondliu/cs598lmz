import types
types.FunctionType = FunctionType

import threading
import time
import sys
import os
import unittest
import rclpy
import rclpy.node
import std_msgs.msg
import builtin_interfaces.msg

from test_msgs.srv import BasicTypes, BasicTypesRequest, BasicTypesResponse

class TestNode(rclpy.node.Node):

    def __init__(self):
        super().__init__('node')
        self.publisher_ = self.create_publisher(std_msgs.msg.String, 'test/topic', 10)
        self.subscription_ = self.create_subscription(std_msgs.msg.String, 'test/topic', self.subscription_callback, 10)
        self.service_ = self.create_service(BasicTypes, 'test/service', self.service_callback)
        self.timer_ = self.create_timer(0.5, self.timer_callback)
        self.spin_thread_ = threading.Thread(target=self.spin)
        self.spin_thread_.start
