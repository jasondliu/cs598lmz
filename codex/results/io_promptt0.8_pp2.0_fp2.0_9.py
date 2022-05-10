import io
# Test io.RawIOBase
print(issubclass(io.RawIOBase, io.IOBase))

import socket
# Test socket.SocketIO
print(issubclass(socket.SocketIO, io.IOBase))

# Test socket.socket
print(issubclass(socket.socket, io.IOBase))
