import select
import socket
import sys
import termios
import tty
import traceback

from . import controls
from .logger_manager import log

def set_raw_term_input(fd):
    """Set stdin to raw-mode.

    The terminal is set to raw mode so that keystrokes are
    returned one at a time, and not buffered-up by the
    terminal.

    """
    old_settings = termios.tcgetattr(fd)
    tty.setraw(fd)
    return old_settings

class Stdin:
    """Manage the stdin file descriptor and ensure it is returned"""
    def __init__(self, stdin):
        self.stdin = stdin
        self.old_settings = set_raw_term_input(self.stdin)

    def __enter__(self):
        return self.stdin

    def __exit__(self, exc_type, exc_val, exc_tb):
        termios.tcsetattr(self.stdin, termios.TCSADRAIN, self.old_settings
