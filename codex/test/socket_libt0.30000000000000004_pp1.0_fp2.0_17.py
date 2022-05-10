import socket
import struct
import sys
import time
import traceback

from . import common
from . import constants
from . import exceptions
from . import utils
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_host_ip = None
_g_host_mac = None
_g_host_name = None
_g_host_uuid = None


def _get_host_ip():
    global _g_host_ip
    if _g_host_ip is None:
        _g_host_ip = utils.get_ip_address()
    return _g_host_ip


def _get_host_mac():
    global _g_host_mac
    if _g_host_mac is None:
        _g_host_mac = utils.get_mac_address()
    return _g_host_mac


def _get_host_name():
    global _g_host_name
    if _g_host_name is None:
        _g_
