import select
import socket
import sys
import threading
import time
import traceback

import paramiko

from . import __version__
from . import common
from . import config
from . import constants
from . import exceptions
from . import utils
from . import x11
from . import xauth
from . import xorg
from . import xserver

LOG = logging.getLogger(__name__)


class XpraServerBase(object):
    """ Base class for an Xpra server.
        Provides all the generic functions but is not tied to a specific backend.
        (ie: Xvfb, Xephyr or Xdummy)
    """
