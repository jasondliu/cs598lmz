import select
import sys
import tty
import termios

from . import common

def getch():
    """Get a single character from stdin.

    Returns:
        The character read from stdin.
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def get_input(timeout=None):
    """Get input from stdin.

    Args:
        timeout: The number of seconds to wait for input. If None, this function
            never returns.

    Returns:
        The input received from stdin.
    """
    if timeout is not None:
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin)
