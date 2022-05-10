import select
import signal
import sys
import time

import numpy as np

from .constants import *
from .exceptions import *
from .protocol import *
from . import util
from . import __version__

# Make sure Python 3.x uses bytes for input
# currently no way to do this in Python 2.x
if sys.version_info[0] >= 3:
    raw_input = input

class PicoHarp300(object):
    """
    The PicoHarp300 object.
    """
    def __init__(self,
                 com_port=None,
                 baud_rate=None,
                 mode=None,
                 verbose=False,
                 **kwargs):
        """
        Create a PicoHarp300 object.

        Parameters
        ----------
        com_port : str, optional
            The name of the port to connect to. If None (default), this
            will use the first port found that is a PicoHarp300.
        baud_rate : int, optional
            The baud rate for the connection. If None (
