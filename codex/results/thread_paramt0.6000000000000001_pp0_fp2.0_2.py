import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import time
import rospy
import baxter_interface
import copy
from baxter_core_msgs.msg import EndpointState
from baxter_core_msgs.msg import SEAJointState
from geometry_msgs.msg import Pose, Point, Quaternion
from std_msgs.msg import (
    UInt16,
)

from baxter_interface import CHECK_VERSION
from baxter_external_devices import getch

#this is for the grippers
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg

from baxter_core_msgs.msg import EndpointState
from geometry_msgs.msg import Pose, Point, Quaternion
#from std_msgs.msg import Header
from sensor_msgs.msg import JointState
from copy import deepcopy

#from sensor_msgs.msg import (
#    Image,
#)

