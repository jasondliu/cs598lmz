import socket
# Test socket.if_indextoname() and socket.if_nametoindex()

import support

import os, sys

try:
    import fcntl
except ImportError:
    print "This test is only applicable on Unix"
    sys.exit(0)

ifname = "lo"
ifname2 = "lo"

# Some platforms may not have lo device
if os.name != "nt":
    try:
        ifname2 = socket.if_indextoname(socket.if_nametoindex(ifname))
    except OSError:
        pass


# On some platforms, the error is different
try:
    socket.if_indextoname(socket.if_nametoindex(ifname) + 1)
except (OSError, socket.error):
    pass
else:
    raise support.TestError("Expected error on invalid index")

try:
    socket.if_nametoindex("")
except (OSError, socket.error):
    pass
else:
    raise support.TestError("Expected error on invalid name")

if ifname2 !=
