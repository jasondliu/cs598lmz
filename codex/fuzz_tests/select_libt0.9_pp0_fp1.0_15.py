import select
import threading
import time
import os
import fcntl

__all__ = ['Error', 'input', 'getpass', 'getuser', 'unix_getpass']


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class Termios:
    # These are the same as for solaris.
    # FIXME: where does the rest come from?
    TCGETS = 0x402c7413
    TCSETS = 0x802c7414
    TCSETSW = 0x402c7415
    TCSETSF = 0x802c7416
    TIOCGWINSZ = 2148037736
    TIOCSWINSZ = 2148037737
    TIOCINQ = 2150175168


class FileWrapper:
    def __init__(self, fd):
        self.fd = fd

    def fileno(self):
        return self.fd


def prepare_terminal(fd):
    fcntl.fcntl(fd, fcntl.F_SETFL,
