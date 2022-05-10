import threading
threading._DummyThread._Thread__stop = lambda x: 42

import rospy
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage

from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

import time

class ImagePublisher():
    def __init__(self):
        rospy.init_node('image_publisher')
        self.image_pub = rospy.Publisher('/camera/image', Image, queue_size=10)
        self.compressed_pub = rospy.Publisher('/camera/compressed', CompressedImage, queue_size=10)
        self.bridge = CvBridge()
        self.cv_image = None
        self.image_width = 640
        self.image_height = 480

        self.camera_index = 0
        if rospy.has_param('~camera_index'):
            self.camera_index = rospy.get_param('~camera_index')

        self.show_image = False
       
