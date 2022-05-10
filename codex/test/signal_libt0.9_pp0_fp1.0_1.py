import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import re
import getpass
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox
from QtEditor.qt_base_classes import *


# GENERAL APPLICATION PARAMETERS
class Qt_Application(QtCore.QObject, object):

    def __init__(self):
        super(Qt_Application, self).__init__()
        self.copyLim = 5000
        self.copyData = list()
        self.lastError = None
        self.lastErrorStatus = 'default'
        self.appName = ''
        self.startDate = -1
        self.lastDataSaved = -1
        self.dataChanged = False
        self.parameters = {'defaultFolder': '', 'fontSize': 14}
        self.applicationPath = os.path.dirname(os.path.realpath(__file__))
        self.set_application_parameters()
