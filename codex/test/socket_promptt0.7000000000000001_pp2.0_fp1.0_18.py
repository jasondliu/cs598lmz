import socket
# Test socket.if_indextoname()
# socket.if_indextoname() translates an interface index to an interface name.
# If there's no interface with the given index, socket.error will be raised.
#
# This test tries to get the name of an interface with an index of some number.
# It expects the interface name to be returned.

import os, sys
from socket_helper import socket_helper
from struct_helper import struct_helper

try:
    import fcntl
except ImportError:
    print("SKIP")
    sys.exit()

try:
    f = os.popen("ip link show")
except:
    print("SKIP")
    sys.exit()

data = f.read()
f.close()

if data.find(" lo: ") == -1:
    print("SKIP")
    sys.exit()

index = int(data[data.index(" lo: ") + 5:data.index(" lo: ") + 7], 16)

# get interface name
