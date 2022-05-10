import weakref

from PyQt5.QtCore import Qt, QObject, QVariant, pyqtSlot, QUrl
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QGuiApplication, QClipboard
from PyQt5.QtQml import QJSEngine, QJSValue
from PyQt5.QtQuick import QQuickView

from .core import TaskAware, Task
from . import resources
from .layout import Layout, UiTile
from .client import QtileProtocol, RawObject, Unpacker
from .log_utils import logger
from .utils import QT_VERSION
from .qtile_window import QtileWindow, QtileWindowList
from . import widgets
from .resources import Resources


class QtileSession:
    """
    Contains all the objects that need to live across qtile restarts.
    """
    def __init__(self):
        self.qtile_protocol = False
        self.layout_list = []


