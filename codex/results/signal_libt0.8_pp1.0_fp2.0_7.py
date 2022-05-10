import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from qgis.PyQt import QtGui, QtCore, QtXml
from qgis.core import *

from mapclientplugins.segmentationstep.mytool import mytool
from mapclientplugins.segmentationstep.mytool import myconfig
from mapclientplugins.segmentationstep.mytool import mylayer

from mapclientplugins.segmentationstep.ui_mainwindow import Ui_MainWindow
from mapclientplugins.segmentationstep.ui_segmentation import Ui_Form
from mapclientplugins.segmentationstep.ui_input import Ui_Form2
from mapclientplugins.segmentationstep.ui_output import Ui_Form3
from mapclientplugins.segmentationstep.ui_preview import Ui_Form4
from mapclientplugins.segmentationstep.ui_visualisation import Ui_Form5
from mapclientplugins.segmentationstep.ui_filemanager import Ui_Form6
from mapclientplugins.segment
