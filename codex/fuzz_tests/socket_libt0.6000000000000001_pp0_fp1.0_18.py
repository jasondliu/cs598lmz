import socket
import os
import sys

import sys
import os
import socket
import struct
import re
import ctypes
import ctypes.util
from subprocess import Popen, PIPE

# On windows, socket.AF_PACKET is not available
if not hasattr(socket, 'AF_PACKET'):
    socket.AF_PACKET = 17

# On windows, socket.AF_NETLINK is not available
if not hasattr(socket, 'AF_NETLINK'):
    socket.AF_NETLINK = 16

# On windows, socket.AF_PPPOX is not available
if not hasattr(socket, 'AF_PPPOX'):
    socket.AF_PPPOX = 24

# On windows, socket.AF_CAN is not available
if not hasattr(socket, 'AF_CAN'):
    socket.AF_CAN = 29

# On windows, socket.AF_TIPC is not available
if not hasattr(socket, 'AF_TIPC'):
    socket.AF_TIPC = 30

#
