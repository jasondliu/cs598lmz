import _struct
import sys
import time

from _thread import start_new_thread
from functools import partial
from multiprocessing import Queue

from PyQt5 import QtCore, QtWidgets

from Models.Objects import *
from Models.Constants import *
from Models.Logger import Logger
from Models.Server import Server
from Views.MainWindow import MainWindow
from Views.SettingsWindow import SettingsWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    SettingsWindow = SettingsWindow()
    MainWindow.show()
    sys.exit(app.exec_())
