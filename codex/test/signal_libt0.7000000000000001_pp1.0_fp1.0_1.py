import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QThreadPool
from PyQt5.QtCore import QRunnable
from PyQt5.QtCore import pyqtSignal
import time
import sys

class Runnable(QRunnable):   
    def __init__(self, target, *args, **kwargs):
        super(Runnable, self).__init__()
        self.target = target
