import types
types.ClassType = type

import sys
sys.path.insert(0, '..')

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignature

from ui.Ui_MainWindow import Ui_MainWindow
from ui.Ui_FileDialog import Ui_FileDialog
from ui.Ui_FilePropertiesDialog import Ui_FilePropertiesDialog
from ui.Ui_PropertiesDialog import Ui_PropertiesDialog
from ui.Ui_AboutDialog import Ui_AboutDialog
from ui.Ui_HelpDialog import Ui_HelpDialog

from ui.FileDialog import FileDialog
from ui.FilePropertiesDialog import FilePropertiesDialog
from ui.PropertiesDialog import PropertiesDialog
from ui.AboutDialog import AboutDialog
from ui.HelpDialog import HelpDialog

from modules.File import File
from modules.Dir import Dir
from modules.FileSystemModel import FileSystemModel
from modules.FileSystemProxyModel import FileSystemProxyModel

