import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from . import utils
from . import config
from . import data
from . import gui
from . import gui_utils
from . import log
from . import qt_utils
from . import resources
from . import settings
from . import tasks
from . import update
from . import widgets

from .data import Data
from .gui import MainWindow
from .gui_utils import GuiUtils
from .log import Log
from .qt_utils import QtUtils
from .settings import Settings
from .tasks import Tasks
from .update import Update
from .widgets import Widgets

from . import __version__

# -----------------------------------------------------------------------------
# Globals
# -----------------------------------------------------------------------------

logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------

