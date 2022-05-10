import ctypes
ctypes.windll.user32.SetProcessDPIAware()
# ----------------------

import traceback
import time
from pathlib import Path
import sys
from exceptions import Exception

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl
from PyQt5 import QtCore
import zmq
import subprocess
from multiprocessing import Process, Pipe


from MainWindowUI import MainWindowUI
from Settings import Settings
from OpticalParam import OpticalParam
from LensType import LensType
from MWinit import MWinit
from Var import Var
from Log import Log, LogExc
from SetOfSlitsCoord import SetOfSlitsCoord
from Backend import Backend


class MW(MainWindowUI):
    def __init__(self, optical_param, setofslitscoord, setofslits, lens_type, pipe):
        super(MW, self).__init__()
        self.optical_param = optical_param
        self.setOfSlits
