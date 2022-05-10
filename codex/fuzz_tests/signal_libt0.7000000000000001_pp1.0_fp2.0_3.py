import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import subprocess
import threading
import re

import gobject

from numpy import *

import pygtk
pygtk.require('2.0')
import gtk
import pango

import matplotlib
matplotlib.use('GTK')
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas

import ConfigParser

class MainWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        
        self.set_title("I2C Sensors Monitor")
        self.set_size_request(1024, 600)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("delete_event", self.delete_event)
        self.connect("destroy", self.destroy)
        
        self.sensors = []

