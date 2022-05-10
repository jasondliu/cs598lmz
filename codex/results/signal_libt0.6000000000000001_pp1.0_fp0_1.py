import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import QThread, SIGNAL

import sys
import os.path
import re
import time
import types
import traceback

sys.path.append("../../")
from cv2 import cv

from ui_mainwindow import *
from ui_about import *
from ui_config import *

from ui_config_camera import *
from ui_config_mapping import *
from ui_config_calibration import *
from ui_config_sample import *
from ui_config_colors import *
from ui_config_filters import *
from ui_config_processing import *
from ui_config_contours import *
from ui_config_objects import *
from ui_config_tracker import *
from ui_config_sensors import *
from ui_config_sensors_dynamic
