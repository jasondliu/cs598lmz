import socket
# Test socket.if_indextoname() with correct interface index.
# Intended to be used on Linux.
# TODO: Does if_indextoname exist on other platforms?

import socket
from socket import *

interface_idx = getifindex('lo')
name = if_indextoname(interface_idx)

print "name:", name
assert(name == 'lo')
