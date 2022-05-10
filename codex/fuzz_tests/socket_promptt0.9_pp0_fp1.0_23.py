import socket
# Test socket.if_indextoname on an i/f that doesn't exist
try:
    socket.if_indextoname(1)
except OSError as e:
    exit(0)
raise RuntimeError("Test FAILED")
