import socket
# Test socket.if_indextoname() and socket.if_nameindex()
import os
import sys

if sys.platform.startswith('darwin'):
    if_indextoname = os.getenv('TEST_INDEXTONAME') or 'en0'
    if_nameindex = os.getenv('TEST_NAMEINDEX') or 'en0'
else:
    if_indextoname = os.getenv('TEST_INDEXTONAME') or 'eth0'
    if_nameindex = os.getenv('TEST_NAMEINDEX') or 'eth0'

index = socket.if_nametoindex(if_indextoname)
if index == 0:
    raise SystemExit('ERROR: Cannot get index of "%s"' % if_indextoname)

name = socket.if_indextoname(index)
if name != if_indextoname:
    raise SystemExit('ERROR: Got wrong interface name: "%s"' % name)

# The following test requires the interface to be up.  Fail gracefully
# if the interface is not up.

