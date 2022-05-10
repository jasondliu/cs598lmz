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
from . import worker_thread

logger = logging.getLogger(__name__)


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A simple GUI for the '
                                                 'Mozilla DeepSpeech STT engine')
    parser.add_argument('--version', action='version',
                        version='%(prog)s ' + version.__version__)
    parser.add_argument('--debug', action='store_true',
                        help='Show debug messages')
    parser.add_argument('--no-update-check', action='store_true',
                        help='Disable update check')
    parser.add_argument('--no-gui', action='store_
