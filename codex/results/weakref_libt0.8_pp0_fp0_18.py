import weakref
import sys

from PyQt5.QtCore import QObject
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QTimer

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import qApp

# make sure extensions have priority to load over default modules.
sys.path.insert(0, os.path.dirname(__file__))

from . import _qrcode


class MainWindow(QWidget):

    def __init__(self):
       
