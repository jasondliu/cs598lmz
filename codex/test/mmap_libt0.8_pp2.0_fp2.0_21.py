import mmap
import numpy as np
import os
import sys
from timeit import default_timer as timer
import time
from copy import copy, deepcopy
from datetime import datetime
from datetime import timedelta
import logging
from multiprocessing import Process, Pipe, Lock, Value
import multiprocessing
from os.path import join
import random
from scipy.io import wavfile
from scipy.signal import get_window
import signal
import string
import subprocess
import threading

import roslib
import rospy
import rosgraph
import rospkg
from std_msgs.msg import Header, Bool
from std_srvs.srv import Empty, EmptyRequest
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayLayout, MultiArrayDimension
from actionlib_msgs.msg import GoalStatus
from sound_play.libsoundplay import SoundClient
