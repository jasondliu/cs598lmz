import select
import socket
import sys
import time

from . import constants
from . import log
from . import util
from . import x11
from .constants import *
from .log import *
from .util import *
from .x11 import *

def connect_to_server(wm_name=None, wm_class=None, display=None):
    """Connect to an existing window manager via ipc. Return an ipc socket
    object, or None if none is found."""

    # See if we can get the display number from the environment
    if display is None:
        try:
            display = int(os.environ["DISPLAY"].split(":")[1])
        except:
            raise ValueError("Could not retrieve DISPLAY env variable, "
                    "please provide display number")

    # Create a socket to communicate with the window manager
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("127.0.0.1", display))
    except socket.error:
        return None

   
