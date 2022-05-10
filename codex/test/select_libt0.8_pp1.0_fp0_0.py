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

