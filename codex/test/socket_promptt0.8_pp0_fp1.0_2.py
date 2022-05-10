import socket
# Test socket.if_indextoname
socket.if_indextoname(100)
# Test socket.if_indextoname(None)
socket.if_indextoname(None)
# Test socket.if_indextoname()
socket.if_indextoname()
# Test socket.if_indextoname(None, None)
socket.if_indextoname(None, None)
# Test socket.if_indextoname(None, None, None)
socket.if_indextoname(None, None, None)
# Test socket.if_indextoname(None, b'foo', None)
socket.if_indextoname(None, b'foo', None)
# Test socket.if_indextoname(None, b'foo', 43)
socket.if_indextoname(None, b'foo', 43)
# Test socket.if_indextoname(43, b'foo', None)
socket.if_indextoname(43, b'foo', None)
# Test socket.if_indextoname(43, b'foo
