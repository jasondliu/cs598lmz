import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import sys
import os
import os.path

import traceback
import re
import time
import pickle
import datetime
import math
import numpy

from array import array
from pymavlink import mavutil

from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from pymavlink.dialects.v10 import ardupilotmega as mavlink

from MAVProxy.modules.lib.mp_settings import MPSettings, MPSetting

from MAVProxy.modules.lib import mp_module
from MAVProxy.modules.lib import mp_util
from MAVProxy.modules.lib import mp_settings

from MAVProxy.modules.mavproxy_map import mp_elevation
from MAVProxy.modules.mavproxy_map import mp_slipmap
from MAVProxy.modules.
