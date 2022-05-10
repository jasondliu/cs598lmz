import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from . import __version__
from . import config
from . import logging_
from . import main_window
from . import resources
from . import settings
from . import utils


def main():
    """
    The main function of the application.
    """
    # Parse command line arguments
    parser = utils.create_argparser()
    args = parser.parse_args()

    # Set up logging
    logging_.setup(args.log_level)

    # Set up application
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(':/icons/icon.png'))
    app.setApplicationName('QtPyVCP')
    app.setApplicationVersion(__version__)

    # Create the main window
    window = main_window.MainWindow()
