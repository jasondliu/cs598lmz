import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import utils
from . import version
from . import websocket

logger = logging.getLogger(__name__)

# A list of all the client instances that are currently connected.
# This is used to keep track of them for the atexit handler.
_instances = []

# The atexit handler that will be called when the program exits.
# This will close all the client instances that are still connected.
def _atexit_handler():
    for instance in _instances:
        instance.close()

atexit.register(_atexit_handler)

