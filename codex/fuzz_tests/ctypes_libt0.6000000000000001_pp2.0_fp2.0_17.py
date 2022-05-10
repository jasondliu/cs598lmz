import ctypes
ctypes.cdll.LoadLibrary('/opt/ros/kinetic/lib/libgazebo_ros_api_plugin.so')

from gazebo_msgs.msg import ModelStates
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray, MultiArrayLayout, MultiArrayDimension
from std_msgs.msg import Int16
from std_msgs.msg import Int16MultiArray, MultiArrayLayout, MultiArrayDimension
import numpy as np
import rospy
import math
import time
import sys
import os

def get_rotation (msg):
    orientation_q = msg.pose[1].orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_
