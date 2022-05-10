import select
import socket
import sys
import threading
import time

from . import config
from . import log
from . import utils
from . import version
from . import x11


class XpraClient(object):
    """
        This is the base class for Xpra clients.
        It provides all the generic functionality,
        the platform specific code is in the platform subclasses.
    """

    def __init__(self):
        self.exit_code = None
        self.exit_on_signal = False
        self.exit_on_disconnect = False
        self.exit_on_last_client_exit = False
        self.exit_with_client = False
