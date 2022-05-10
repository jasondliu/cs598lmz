import select
import fcntl
import sys
import time
import atexit
import logging

from itertools import chain
from collections import namedtuple

import pyudev

try:
    from sarge import run, Capture
except ImportError:
    raise ImportError("You need to install the sarge package to use this module.")

# TODO create as class and sent over as arg
log = logging.getLogger(__name__)


