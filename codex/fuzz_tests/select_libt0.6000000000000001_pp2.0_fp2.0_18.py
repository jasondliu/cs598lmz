import select
import subprocess

from . import tty_escape
from . import util


def _get_terminal_size():
    """
    Get terminal size (columns and rows)
    """
    try:
        return (int(os.environ.get('COLUMNS', '80')),
                int(os.environ.get('LINES', '24')))
    except ValueError:
        return (80, 24)


def _get_terminal_width():
    """
    Get terminal width (columns)
    """
    try:
        return int(os.environ.get('COLUMNS', '80'))
    except ValueError:
        return 80


def _get_terminal_height():
    """
    Get terminal height (rows)
    """
    try:
        return int(os.environ.get('LINES', '24'))
    except ValueError:
        return 24


def _get_terminal_fg_color():
    """
    Get terminal foreground color
    """
    return int(os.environ
