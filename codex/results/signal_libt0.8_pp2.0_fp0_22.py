import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
from random import uniform

from Ui_MainWindow import Ui_MainWindow
from Sensor_List import *
from Somato_Sensory_List import *
from Vibro_List import *
from Vibro_List2 import *
from Audio_List import *
from Common_List import *

from Sensor_List import *
from Somato_Sensory_List import *
from Vibro_List import *
from Vibro_List2 import *
from Audio_List import *
from Common_List import *
from version import version
import threading
from Queue import Queue

from Serial_Communication import Serial_Packet
from ctypes import *
from sys import platform as _platform
from Calibration_UI import *
from Send_EMG_Haptic_UI import *
from Send_
