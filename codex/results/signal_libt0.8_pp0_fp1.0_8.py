import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui, uic

# For loading QtDesigner UI files
import os
uifile = os.path.join(os.path.dirname(__file__), '../CCDCGUI.ui')
CCDCGui, CCDCGuiBase = uic.loadUiType(uifile)
CCDCGui, CCDCGuiBase = uic.loadUiType(uifile)

import numpy as np
import time

import CCDCData
import CCDCSettings
import CCDCCamera
import CCDCImage
import CCDCLog

import ccdc_display as cd

import scipy.stats as ss

from datetime import datetime

import CCDCLogging

# This class is the main application window of the CCDC program.
class CCDCGuiApp(QtGui.QMainWindow, CCDCGui):
    def __init__(self):
        super(self.__
