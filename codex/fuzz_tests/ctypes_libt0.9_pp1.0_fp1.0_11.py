import ctypes
ctypes.cdll.LoadLibrary('./lib/libroslib.so')

import roslib
roslib.load_manifest('mcr_robot_model_navigation')

import rospy
import tf

from moveit_commander import *
import actionlib_msgs.msg as actionlib_msg
from mcr_robot_model_navigation.perform_head_motion import *

# from mcr_robot_model_navigation.srv import MotionPreparation
from mcr_perception_msgs.srv import RobotBaseAction
from mcr_perception_msgs.srv import AreObjectsStored

import moveit_commander.conversions as mc

import geometry_msgs.msg as geometry_msgs

class RobotBase(object):
    #PRE_GRASPING_HEIGHT = 0.13 # in the air
    #PRE_GRASPING_HEIGHT = 0.061 # on the table
    PRE_GRASPING_HEIGHT = 0.051 # on the table
    PICK_
