import socket
import struct
import sys
import time

import numpy as np

from . import _utils
from . import _constants
from . import _errors

# =============================================================================
#
# =============================================================================

def _get_socket(host, port):
    """
    Returns a socket object for the given host and port.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

# =============================================================================
#
# =============================================================================

def _get_bytes(s, n):
    """
    Returns n bytes from the socket s.
    """
    b = b''
    while len(b) < n:
        b += s.recv(n - len(b))
    return b

# =============================================================================
#
# =============================================================================

def _get_string(s, n):
    """
    Returns a string of length n from the socket s.
    """
    return _get_bytes(s, n).decode('ascii')

# =============================================================================
