import socket
import sys
import time

from . import config
from . import log
from . import util
from . import version

# -----------------------------------------------------------------------------
#
# CONSTANTS
#
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#
# FUNCTIONS
#
# -----------------------------------------------------------------------------

def get_hostname():
    """
    Return the hostname of the machine.
    """
    return socket.gethostname()

def get_ip_address():
    """
    Return the IP address of the machine.
    """
    return socket.gethostbyname(get_hostname())

def get_mac_address():
    """
    Return the MAC address of the machine.
    """
    return util.get_mac_address()

def get_system_info():
    """
    Return a dictionary of system information.
    """
