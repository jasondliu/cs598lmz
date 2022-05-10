import socket
import sys
import threading
import time

import cv2
import numpy as np

import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image


class ImageSender(threading.Thread):
    def __init__(self, host, port, cv_image):
        super(ImageSender, self).__init__()
        self.host = host
        self.port = port
        self.cv_image = cv_image

    def run(self):
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        result, imgencode = cv2.imencode('.jpg', self.cv_image, encode_param)
        data = np.array(imgencode)
        stringData = data.tostring()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
