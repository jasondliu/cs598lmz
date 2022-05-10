import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time

from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from pyqtconfig import Ui_ConfigDialog

import rtlib.config
import rtlib.load_program
import rtlib.logfiles
import rtlib.interface
import rtlib.programs

from .common import debug_trace

## \package rtlib.ui.workstation

## \brief QT UI for RT workstation
#
#  Handles the start/stop of the communication interface, calls the handlers
#  from rtlib.interface and displays the information from the programs.
#
#  \ingroup qtui

## Last UI update time as unix timestamp
last_update_time=0


## ////////////////////// WORKSTATION UI  class //////////////////////

class Workstation( QtWidgets.QWidget):

    ## \internal \brief
