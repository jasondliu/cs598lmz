import socket
import struct

from subprocess import Popen, PIPE, STDOUT

from .constants import *
from .exceptions import *

"""
A simple module to get the IP address of your Linux machine
"""

__all__ = [
    'get_ip_address',
    'get_interface_ip',
    'get_lan_ip',
    'Wlan',
    'Eth'
]

"""
Gets the IP address of your machine.

This is a simple function that uses several methods to get the ip address of a
Linux machine.

Returns the IP address of the machine.
"""
def get_ip_address():
    """
    Get the IP address of the machine.

    Returns the IP address of the machine.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
    except:
        ip_address =
