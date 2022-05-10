import weakref

from PyQt5.QtCore import Qt, QObject, QThread, QTimer, QEvent, pyqtSignal
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont, QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget, \
    QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QScrollArea, \
    QFrame, QMenu, QMessageBox, QFileDialog, QTabWidget, QPushButton

from . import appdirs
from . import __version__
from . import __versiontag__
from . import __windowsversion__
from . import __url__
from . import __macosxversion__
from . import __license__
from . import __author__
from . import __author_email__
from . import __python_version__
from . import __qt_version__
from .about import About
from .config import Config
from .constants import *
from .devlist import DeviceList
from
