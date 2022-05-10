import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# GUI
from PyQt5 import QtCore, QtWidgets, QtGui
from . import gui
from . import config
from . import printers
from . import comms
from . import gcode_processor
from . import about
from . import calibrate
from . import start_gcoder
from . import temp_control
from . import upgrade
from . import gcode

import threading
import sys
import time
import struct
import numpy as np

#############################################################################################
###############################     MAIN APPLICATION      ###################################
#############################################################################################

class MainApp(QtWidgets.QApplication):
    """Main application class, contains main loop and global data."""
    #### CONSTANTS ####
    # Timeout for main loop
    TICK_PERIOD = 0.01

    # Status values
    OFFLINE = 0
    ONLINE = 1
    PRINTING = 2
    PAUSED = 3

    #### SIGNALS #
