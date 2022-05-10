import select
import sys
import time

from . import log
from . import util
from . import x11

#
# Constants
#

#
# Functions
#

def _get_window_id(window):
    """Get the window ID of a window.

    The window ID is a string that uniquely identifies a window.

    Args:
        window (str): The window name.

    Returns:
        str: The window ID.

    """
    return x11.get_window_id(window)

def _get_window_name(window_id):
    """Get the window name of a window.

    The window name is the name of the window as it appears in the title bar.

    Args:
        window_id (str): The window ID.

    Returns:
        str: The window name.

    """
    return x11.get_window_name(window_id)

def _get_window_title(window_id):
    """Get the window title of a window.

    The window title is the name of the window as it appears in the title
