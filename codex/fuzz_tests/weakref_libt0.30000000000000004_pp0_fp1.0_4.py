import weakref

from . import config
from . import core
from . import util
from . import widgets
from . import _version

logger = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow):
    """
    The main window of the application.
    """

    def __init__(self, app):
        super().__init__()

        self.app = app
        self.app.aboutToQuit.connect(self.app_about_to_quit)

        self.setWindowTitle("{} {}".format(config.APP_NAME, _version.__version__))
        self.setWindowIcon(QtGui.QIcon(config.APP_ICON_PATH))

        self.setCentralWidget(widgets.MainWidget(self))

        self.create_actions()
        self.create_menus()
        self.create_toolbar()

        self.setMinimumSize(config.MAIN_WINDOW_MIN_WIDTH, config.MAIN_WINDOW_MIN_HEIGHT)
        self.
