import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# import the Qt libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

# import the QGIS libraries
from qgis.core import *
from qgis.gui import *

# import the configuration
from configuration import *

# import the global variables
from global_variables import *

# import the map tools
from map_tools import *

# import the utilities
from utilities import *

class MainWindow(QMainWindow):
    def __init__(self, iface):
        # initialize the super class
        QMainWindow.__init__(self, None)
        
        # set the interface
        self.iface = iface
        
        # set the window title
        self.setWindowTitle(self.tr('QGIS Web Client'))
        
