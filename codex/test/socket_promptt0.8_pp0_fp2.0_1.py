import socket
# Test socket.if_indextoname
import time
import gettext
import ctypes
from ctypes import *
from ctypes.wintypes import *
import winerror
 
#
# =============================================================
#
# Win32 definitions
#
# The following definitions are from the Windows Platform SDK,
# and are needed for the WSAIoctl call to return the adapter
# MAC addresses.
#
# =============================================================
#
 
# Manifest constants used by the WSAIoctl call
 
SIO_GET_INTERFACE_LIST = 0x4004747F
SIO_GET_INTERFACE_LIST_EX = 0x40047469
 
GAA_FLAG_SKIP_ANYCAST = 0x0002
GAA_FLAG_SKIP_MULTICAST = 0x0004
GAA_FLAG_SKIP_DNS_SERVER = 0x0008
GAA_FLAG_INCLUDE_PREFIX = 0x0010
GAA_FLAG_SKIP_FRIENDLY_NAME = 0x0020
GAA_FLAG_INCLUDE_WINS_INFO = 0x00
