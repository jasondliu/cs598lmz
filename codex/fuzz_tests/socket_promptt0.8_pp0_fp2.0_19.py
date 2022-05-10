import socket
# Test socket.if_indextoname
socket.if_indextoname(1)

import _socket
# Test _socket.if_indextoname
_socket.if_indextoname(1)

import subprocess
# Test subprocess.Popen
subprocess.Popen(['ls', '-l'])

import sys
# Test sys.setdlopenflags
sys.setdlopenflags(1)

import termios
# Test termios.tcdrain
termios.tcdrain(-1)

import time
# Test time.clock
time.clock()

import unix
# Test unix.fcntl
unix.fcntl(-1, unix.F_SETFL, 0)
unix.fcntl(-1, unix.F_SETLK, 0)
unix.fcntl(-1, unix.F_SETLKW, 0)
unix.fcntl(-1, unix.F_GETFL, 0)
unix.fcntl(-1, unix.F_GETLK, 0)
unix.fc
