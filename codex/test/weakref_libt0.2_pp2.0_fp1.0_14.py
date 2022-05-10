import weakref
import logging

from PyQt5.QtCore import QObject, pyqtSignal, QThread, QTimer
from PyQt5.QtWidgets import QApplication

from . import utils
from . import config
from . import settings
from . import models
from . import exceptions
from . import tasks
from . import signals
from . import events
from . import plugins
from . import ui
from . import log
from . import resources
from . import __version__


logger = logging.getLogger(__name__)


class Application(QObject):
    """
    Main application class.

    :param parent: Parent object.
    :type parent: :class:`PyQt5.QtCore.QObject`
    """

    #: Signal emitted when the application is about to quit.
    aboutToQuit = pyqtSignal()

    #: Signal emitted when the application is about to start.
    aboutToStart = pyqtSignal()

    #: Signal emitted when the application is started.
    started = pyqtSignal()

    #:
