import select
import socket
import sys
import termios
import tty

from . import __version__
from . import config
from . import const
from . import log
from . import util
from . import x11

logger = log.get_logger(__name__)


def _get_tty_size():
    """Get the size of the current terminal.

    Returns:
        A tuple of (rows, cols).
    """
    rows, cols = os.popen('stty size', 'r').read().split()
    return int(rows), int(cols)


def _get_tty_attr():
    """Get the attributes of the current terminal.

    Returns:
        A termios.tcgetattr() compatible object.
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    return old_settings

