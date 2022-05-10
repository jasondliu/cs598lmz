import socket
# Test socket.if_indextoname, socket.if_nametoindex
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
socket.if_indextoname(749078)
try:
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
except AttributeError:
    print("SKIP")
    raise SystemExit

try:
    socket.if_nametoindex("lo0")
except OSError as e:
    print("OSError:", e)
    print("SKIP")
except AttributeError:
    print("SKIP")
