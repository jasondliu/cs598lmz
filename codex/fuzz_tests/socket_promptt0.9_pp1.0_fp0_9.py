import socket
# Test socket.if_indextoname() (see issue #3602).
import _testcapi
try:
    socket.if_indextoname(_testcapi.INT_MAX+1)
except ValueError:
    pass
try:
    socket.if_indextoname(_testcapi.UINT_MAX+1)
except ValueError:
    pass
