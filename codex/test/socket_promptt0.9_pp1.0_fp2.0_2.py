import socket
# Test socket.if_indextoname()
#
# From http://docs.python.org/lib/module-socket.html

import os, sys
import time
from test import support
import socket

support.requires('net')

# Check error conditions
try:
    socket.if_indextoname(-1)
except OSError as x:
    type, errmsg = x.args
    if type != errno.ENXIO:
        raise
else:
    raise Exception('expected an error')

try:
    socket.if_indextoname(0x10000)
except OSError as x:
    type, errmsg = x.args
    if type != errno.ENXIO:
        raise
else:
    raise Exception('expected an error')

# list all the interfaces available on a system
# and can be translated to their interface name
