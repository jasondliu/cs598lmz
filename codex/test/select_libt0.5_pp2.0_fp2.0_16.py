import select
import socket
import threading
import time

from . import exceptions
from . import utils

_logger = logging.getLogger(__name__)


class Server:
    """
    A server that listens for incoming connections and handles them in a separate thread.
    """
