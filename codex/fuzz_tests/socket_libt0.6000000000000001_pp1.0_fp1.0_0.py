import socket
import time
import math
import numpy as np
import cv2
from threading import Lock
from threading import Thread
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# Variables for image processing
img_height = 0
img_width = 0

# Variables for vision commands
vision_commands = ""

# Variables for robot control
robot_vel = 0
robot_rot = 0

def vision_commands_callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	global vision_commands
	vision_commands = data.data

def robot_vel_callback(data):
	global robot_vel
	robot_vel = data.data

def robot_rot_callback(data):
	global robot_rot
	robot_rot = data.data

def image
