import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from . import mainwindow
from . import settings
from . import utils
from . import updater
from . import version
from . import worker


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("PixivUtil2")
    app.setApplicationVersion(version.version)
    app.setOrganizationName("PixivUtil2")
    app.setOrganizationDomain("pixiv.net")

    utils.setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("PixivUtil2 %s", version.version)

    # load settings
    settings.load()

    # check for updates
    if settings.get("check_for_updates"):
        updater.check_for_updates()

    # setup worker
    worker.setup()
