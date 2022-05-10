import select
import threading

# import rospy
import tf.transformations as tft
import numpy as np

# import std_msgs.msg
# import geometry_msgs.msg

# import ar_track_alvar.msg
# import gazebo_msgs.msg

from hpp_ros_base import _get_robot_list
import hpp.corbaserver.robot

class ParseHPPURDFPython(subprocess.Popen):
    def __init__(self, args, directory, nb_robot=1, **kwargs):
        roslib.load_manifest('hpp_ros_base')
        self._global_frame = '/world'
        self._interaction_frame = '/world'

        self._distal_link = '0'
        self._proximal_link = '1'
        self._ignore_frames = list()
