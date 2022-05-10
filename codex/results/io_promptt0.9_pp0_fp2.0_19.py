import io
# Test io.RawIOBase method
io.RawIOBase()
# Test io.BufferedIOBase method
io.BufferedIOBase()
# Test io.TextIOBase method
io.TextIOBase()
# Test io.IOBase method
io.IOBase()
# Test io.FileIO method...
try:
    io.FileIO()
except TypeError:
    pass

# Subprocess module.
import subprocess
# Test subprocess.STARTUPINFO method
subprocess.STARTUPINFO()

# Socket module.
import socket
# Test socket.socket before CBFS 20
socket.socket()
# Test socket.socket to test CBFS 20
try:
    socket.socket(kind=2)
except TypeError:
    pass
# Test socket.socket(kind=4) to test for CBFS 27
try:
    socket.socket(kind=4)
except TypeError:
    pass

# Socketserver module.
import socketserver
socketserver.TCPServer()

# String module
import string
# Test string constants. Always defined.
string.whitespace
# Test
