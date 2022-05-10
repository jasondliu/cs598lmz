import socket
import sys
import threading
import time

import numpy as np

from .sender import Sender
from .receiver import Receiver
from .constants import *
from .utils import *
from . import exceptions

class Connection(object):
    """A class that represents a connection between two nodes."""

    def __init__(self, local_id, local_address, remote_id, remote_address):
        """Initialize a connection.

        Args:
            local_id (int): The local node's id.
            local_address (tuple): The local node's address.
            remote_id (int): The remote node's id.
            remote_address (tuple): The remote node's address.

        """
        self.local_id = local_id
        self.local_address = local_address
        self.remote_id = remote_id
        self.remote_address = remote_address

