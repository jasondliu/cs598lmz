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
