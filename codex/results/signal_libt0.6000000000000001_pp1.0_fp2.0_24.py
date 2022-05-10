import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets

from . import __version__
from . import config
from . import utils
from . import widgets

from .widgets.main_window import MainWindow

from . import _

_logger = logging.getLogger(__name__)


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser(
        description=_('configure and manage a Redis instance'),
        epilog=_('Visit https://github.com/pogodin/redis-commander for help.'),
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s v' + __version__,
    )
    parser.add_argument(
        '--log',
        default='warning',
        help=_('
