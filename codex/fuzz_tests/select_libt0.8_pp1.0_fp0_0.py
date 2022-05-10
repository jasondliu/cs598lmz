import select
import sys
import threading
from socket import *
from . import pudb

# from PyQt4.QtCore import QCoreApplication
# from PyQt4.QtGui import QApplication

try:
    import pyfirmata
    import pyfirmata.boards
    import pyfirmata.serial
except ImportError:
    pyfirmata = None

from . import serial

from . import serial.serialposix
from . import serial.serialwin32
from . import serial.serialjava
from . import serial.serialutil


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal
