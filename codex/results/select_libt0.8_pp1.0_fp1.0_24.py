import selectors
import time
import signal
import socket
import sys
import ctypes
import ctypes.util
import struct
import signal

# sel = selectors.DefaultSelector()
#
# def perform_read(key, mask):
#     bytes_read = key.fileobj.recv(10000)  # Should be ready
#     if bytes_read:
#         print("received", repr(bytes_read), "from connection", key)
#     else:
#         print("closing connection", key)
#         sel.unregister(key.fileobj)
#         key.fileobj.close()
#
# def perform_accept(key, mask):
#     conn, addr = key.fileobj.accept()
#     print("accepted connection from", addr)
#     conn.setblocking(False)
#     key = sel.register(conn, selectors.EVENT_READ, perform_read)
#
# sock = socket.socket()
# sock.bind(("127.0.0.1", 8080))
# sock.listen(100)

