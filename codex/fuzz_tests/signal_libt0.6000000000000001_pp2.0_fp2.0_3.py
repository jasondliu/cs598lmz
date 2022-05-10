import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, QtGui, QtCore


from gui import Ui_MainWindow
from gui2 import Ui_MainWindow2
from gui3 import Ui_MainWindow3

from threading import Thread
import threading
import time
from time import sleep
from playsound import playsound

from threading import Thread
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QThreadPool
from PyQt5.QtCore import QRunnable

import socket
import sys
import random
import os
import subprocess
import datetime
import tkinter
import
