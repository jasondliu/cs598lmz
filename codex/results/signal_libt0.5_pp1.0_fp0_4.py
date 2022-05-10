import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Load the Qt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

# Initialize Qt and QGIS Application
QgsApplication.setPrefixPath("/usr", True)
qgs = QgsApplication([], True)
qgs.initQgis()

# Add the path to Processing framework  
sys.path.append('/usr/share/qgis/python/plugins') 

# Import and initialize Processing framework
from processing.core.Processing import Processing
Processing.initialize()
from processing.tools import *

# Import and initialize Processing provider
import processing
from processing.tools import *
from processing.core.Processing import Processing
Processing.initialize()
from processing.tools import *
from qgis.analysis import *

# Set the current project to the one containing the layers
qgs.addMapLayer(Q
