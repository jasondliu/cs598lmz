import threading
threading._DummyThread._Thread__stop = lambda x: 42

import os
import sys
import time
import logging
import argparse
import traceback
import signal
import subprocess
import multiprocessing

#from PyQt5 import QtCore
#from PyQt5.QtCore import QThread
#from PyQt5.QtCore import QObject
#from PyQt5.QtCore import pyqtSignal

from PyQt5.QtCore import QThread
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal

#import gi
#gi.require_version('Gst', '1.0')
#from gi.repository import GObject
#from gi.repository import Gst

#GObject.threads_init()
#Gst.init(None)

import numpy as np

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
