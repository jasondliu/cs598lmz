import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# Import the compiled UI module
import RS_GUI

#Import the libraries from the python-midi package
from midi import *
from midi.sequencer import Sequencer
import time

import sys
import serial, string
import numpy as np

#ser_port = '/dev/ttyACM0'
ser_port = '/dev/ttyUSB0'
baud_rate = 1000000

#How many samples should we wait before we save a new file?
#The inner loop waits 20 us to read the arduino, so lets have 20/20=1 samples/second
num_samples = 1800

#Global flag to stop acquisition
global_flag = False

#This is how you can read in a file for properties of the instrument
#each line in the file should only have 1 entry, the value
d = {}
with open('
