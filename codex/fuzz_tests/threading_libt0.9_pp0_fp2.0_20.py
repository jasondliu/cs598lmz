import threading
threading.stack_size(67108864)

from jsonrpclib import Server
import lxml.etree
import websocket

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread, SIGNAL
from PyQt4.QtGui import QVBoxLayout, QHBoxLayout, QWidget, QLabel

from gui import TRXDock
from gui import TRXDockWidget

from scr.util import TR
from scr.util import TRX
from scr.util import TRX_PYEZ
from scr.util import TRX_NETCONF

from scr.util import TRDock
from scr.util import TRDockWidget
from scr.util import TRWSClient

from scr.MainController import MainController
from scr.MainWindow import MainWindow
from scr.DeviceConfig import DeviceConfig

VERSION = 0.1

bOpen = True

class MainControllerGUI(MainController):

    def __init__(self,configFile):
        #MainController.__init__(self,configFile)
       
