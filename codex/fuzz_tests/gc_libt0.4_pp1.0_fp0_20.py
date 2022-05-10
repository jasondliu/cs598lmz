import gc, weakref
import logging
log = logging.getLogger(__name__)

from PyQt4.QtCore import QObject, QTimer, QEventLoop
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import pyqtSignal as Signal

from .. import core
from .. import utils
from .. import qt4support as qt4
from . import base
from . import resources

class QThreadManager(QObject):
    """
    Manages a pool of QThreads.

    This is a singleton class.
    """
    _instance = None
    _threads = {}
    _lock = threading.Lock()

    def __new__(cls):
        """
        Create a new instance of QThreadManager, or return the existing
        instance if one already exists.
        """
        if cls._instance is None:
            cls._instance = QObject.__new__(cls)
        return cls._instance

    def __init__(self):
        """
        Initialize the thread manager.

