import socket
# Test socket.if_indextoname()
try:
    assert socket.if_indextoname(1)
except (ValueError, OSError):
    pass
# Test socket.if_nameindex()
try:
    assert socket.if_nameindex()
except (ValueError, OSError):
    pass
# Test socket.if_nametoindex()
try:
    assert socket.if_nametoindex('eth0')
except (ValueError, OSError):
    pass
