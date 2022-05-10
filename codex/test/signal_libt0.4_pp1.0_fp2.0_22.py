import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PySide import QtGui, QtCore

from . import __version__
from . import __author__
from . import __email__
from . import __website__
from . import __description__

from .widgets.main_window import MainWindow
from .widgets.settings_dialog import SettingsDialog
from .widgets.about_dialog import AboutDialog
from .widgets.update_dialog import UpdateDialog

from .utils import get_settings
from .utils import get_stylesheet
from .utils import get_icon
from .utils import get_logger

from .utils import get_update_info
from .utils import get_update_url


class Application(QtGui.QApplication):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)

        self.setApplicationName("QtPyVCP")
        self.setApplicationVersion(__version__)
        self.setOrgan
