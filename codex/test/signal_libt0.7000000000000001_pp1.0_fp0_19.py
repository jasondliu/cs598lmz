import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from ui_editor import Ui_Editor
from ui_newfield import Ui_NewField
from ui_mergefeatures import Ui_MergeFeatures
from ui_mapextent import Ui_MapExtent
from ui_scheduler import Ui_Scheduler
from ui_about import Ui_About
from ui_gps_main import Ui_GPSMain
from ui_fieldmapping import Ui_FieldMapping
from ui_newproject import Ui_NewProject
from ui_select_project import Ui_SelectProject
from ui_featureattributes import Ui_FeatureAttributes
from ui_report import Ui_Report
