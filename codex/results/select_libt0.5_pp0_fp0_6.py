import select
import socket
import sys
import threading
import time

from . import utils
from . import protocol
from . import __version__

logger = logging.getLogger('btsync')

class BTSync(object):
    """
    A class for interacting with a BTSync instance.
    """

    def __init__(self, host='127.0.0.1', port=8888, username=None, password=None):
        """
        Initialize a BTSync instance.
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        self.sock = None
        self.sock_file = None
        self.sock_thread = None
        self.sock_thread_stop = False

        self.id = None
        self.version = None
        self.device_name = None

        self.folders = {}

        self.folder_callbacks = {}
        self.file_callbacks = {}

        self.callbacks_lock = threading.Lock
