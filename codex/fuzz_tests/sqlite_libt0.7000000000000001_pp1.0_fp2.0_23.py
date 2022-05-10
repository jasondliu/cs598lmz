import ctypes
import ctypes.util
import threading
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

import sys
sys.path.append('../')
import pyinterface

import logging
sys.path.append('../')
import logger_utils


class pc_ctrl_window(object):
    """ 
    pc_ctrl_window consists pc_ctrl_window class
    and other functions related to window.
    """
    
    def __init__(self):
        self.window_name = 'pc_ctrl_window'
        
    def setupUi(self, pc_ctrl_window):
        pc_ctrl_window.setObjectName(self.window_name)
        pc_ctrl_window.setWindowModality(QtCore.Qt.WindowModal)
        pc_ctrl_window.resize(240, 500)
        pc_ctrl_window.setMinimumSize(QtCore.QSize(240, 500))
        pc_ctrl_window.setMaximumSize(QtCore.QSize(240, 500))
        pc_ctrl_window.setWindowTitle(self.
