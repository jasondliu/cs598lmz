import socket
# Test socket.if_indextoname() on some common interface indexes.
if socket.if_indextoname(1) != 'lo':
    raise TestFailed('if_indextoname(1) != "lo"')
if socket.if_indextoname(2) != 'eth0':
    raise TestFailed('if_indextoname(2) != "eth0"')
if socket.if_indextoname(3) != 'wlan0':
    raise TestFailed('if_indextoname(3) != "wlan0"')
# Test socket.if_indextoname() on nonexistent indexes.
try:
    socket.if_indextoname(0)
    raise TestFailed('Expected OSError for nonexistent index 0')
except OSError as e:
    if e.errno != errno.ENXIO:
        raise TestFailed('Expected OSError with errno.ENXIO for nonexistent index 0, got ' + str(e))
try:
    socket.if_indextoname(4)
    raise TestFailed
