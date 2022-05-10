import socket
# Test socket.if_indextoname() if present
try:
    socket.if_indextoname(1)
    haveIf_indextoname = True
except AttributeError:
    haveIf_indextoname = False

import threading
import time

from BTL.platform import app_name, app_version
from BTL.defer import Deferred

DEBUG = False

#
# BitTorrent protocol constants
#
# Message types
CHOKE = 0
UNCHOKE = 1
INTERESTED = 2
NOT_INTERESTED = 3 
HAVE = 4
BITFIELD = 5
REQUEST = 6
PIECE = 7
CANCEL = 8
PORT = 9

# Extended message types
HANDSHAKE = 20
KEEPALIVE = 21
SUGGEST_PIECE = 22
HAVE_ALL = 23
HAVE_NONE = 24
REJECT_REQUEST = 25
ALLOWED_FAST = 26
LTEP = 27  # http://www.bittorrent.org/beps/bep_0027.html
# I2P:
