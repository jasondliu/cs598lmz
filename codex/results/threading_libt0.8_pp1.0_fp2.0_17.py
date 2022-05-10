import threading
threading.stack_size(2 ** 27)

from win32event import CreateMutex
from win32api import CloseHandle, GetLastError
from winerror import ERROR_ALREADY_EXISTS
from configparser import ConfigParser
import sys

class App(QtGui.QApplication):

    def __init__(self, *argv):
        QtGui.QApplication.__init__(self, *argv)
        self.setApplicationName("eTests")
        self.setOrganizationName("eTests")
        self.createConfig()
        self.createMutex()
        if self.isRunning() and not hasattr(sys, 'frozen'):
            sys.exit(0)
        self.main = MainWindow()
        self.main.show()
        self.connect(self, QtCore.SIGNAL("lastWindowClosed()"),
                     self.byebye )
    def createConfig(self):
        self.config = ConfigParser()
        if not os.path.isfile("eTests.ini"):
            self.config.add_
