import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThreadPool

from . import config
from . import __version__
from . import utils
from . import widgets
from . import work
from . import resources

logger = logging.getLogger(__name__)


class MainWindow(widgets.MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle(f"{config.APP_NAME} v{__version__}")
        self.setWindowIcon(resources.get_icon("app.png"))

        self.setMinimumSize(800, 600)

        self.thread_pool = QThreadPool()
        self.thread_pool.setMaxThreadCount(1)

        self.init_ui()

    def init_ui(self):
        self.init_menu()
        self.init_toolbar()
        self.
