import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from . import main_window
from . import settings
from . import utils
from . import log
from . import config
from . import update
from . import version
from . import resources
from . import plugins
from . import qt_utils
from . import qt_client
from . import qt_server
from . import qt_settings
from . import qt_update
from . import qt_plugins
from . import qt_log
from . import qt_config
from . import qt_resources
from . import qt_version
from . import qt_about
from . import qt_help
from . import qt_shortcuts
from . import qt_tray
from . import qt_notifications
from . import qt_systray
from . import qt_preferences
