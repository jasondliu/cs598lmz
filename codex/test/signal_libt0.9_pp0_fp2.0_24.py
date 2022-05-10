import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtPrintSupport import  *
import sys
from threading import Timer, Thread, Event
from time import sleep

from PyQt5 import QtWebEngineWidgets


class BlinkThread(Thread):
    def __init__(self, label, icon1, icon2, interval=0.5):
        Thread.__init__(self)
        self.label = label
        self.icon1 = icon1
        self.icon2 = icon2
        self.interval = interval
        self._stopevent = Event()
        self._sleepperiod = 1.0
    
    
    
    
    
    def run(self):
        
        i = True

