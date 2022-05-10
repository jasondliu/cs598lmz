import mmap
# Test mmap.mmap
m = mmap.mmap(0, 16)
m.read(16)
# mmap.mmap is unbound, should not be found

import os
# Test os.lstat
os.lstat("/")
# os.lstat is bound, should be found

import pty
# Test pty.Master
pty.Master()
# pty.Master is unbound, should not be found

import socket
# Test socket.gethostbyname
socket.gethostbyname("localhost")
# socket.gethostbyname is bound, should be found

# Test socket.socket (bound in another module)
s = socket.socket()
s.connect(("localhost", 80))
# socket.socket is unbound, but should not be found

import tempfile
# Test tempfile.mkstemp
tempfile.mkstemp()
# tempfile.mkstemp is bound, should be found

import termios
# Test termios.tcgetattr
termios.tcgetattr(0)
# termios.tcgetattr is bound, should be found

