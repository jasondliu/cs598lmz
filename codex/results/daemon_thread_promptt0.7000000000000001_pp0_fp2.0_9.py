import threading
# Test threading daemon
import multiprocessing
#from multiprocessing import Process, Value, Array
import multiprocessing.dummy
from multiprocessing.dummy import Pool as ThreadPool

from collections import defaultdict

from ctypes import *
from ctypes.wintypes import HANDLE
#from random import randint
from random import randrange

from PyQt4.QtGui import QDialog, QApplication, QColor, QPainter, QFileDialog
from PyQt4.QtCore import Qt, QPoint, QEvent, QSize, QTime, QTimer, QThread, pyqtSignal

from mainwindow_ui import Ui_MainWindow
from info_ui import Ui_Dialog
from settings_ui import Ui_SettingsDialog
from about_ui import Ui_AboutDialog

from config import config
from utils import *

from ntqueryvirtualmemory import ntqueryvirtualmemory
from process_viewer import ProcessViewer

from data import *

from PyQt4.QtGui import QWidget
from PyQt4.Qt
