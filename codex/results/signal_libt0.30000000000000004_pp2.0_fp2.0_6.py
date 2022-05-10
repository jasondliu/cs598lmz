import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from . import config
from . import main_window
from . import utils
from . import log

logger = log.get_logger(__name__)


def main():
    utils.init_config()
    app = QApplication(sys.argv)
    app.setApplicationName(config.APP_NAME)
    app.setOrganizationName(config.ORG_NAME)
    app.setOrganizationDomain(config.ORG_DOMAIN)
    app.setApplicationVersion(config.APP_VERSION)
    app.setStyleSheet(utils.load_stylesheet())

    window = main_window.MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
