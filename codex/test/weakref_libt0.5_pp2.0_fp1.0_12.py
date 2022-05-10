import weakref
import time
import math
import numpy as np
import cv2
import os
import sys
import threading
import Queue
import logging
import logging.config

# GUI
import Tkinter as tk
import ttk
import tkFileDialog
import tkMessageBox

# ROS
import rospy
import roslib
import tf
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String

# Local
from camera import Camera
from calibration import Calibration

# Global variables
logger = None
