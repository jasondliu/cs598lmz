import socket
# Test socket.if_indextoname()
import os
import sys
import fcntl
import struct

if sys.platform == 'win32':
    raise SystemExit("if_indextoname not supported on Windows")

if not hasattr(socket, 'if_indextoname'):
    raise SystemExit("if_indextoname not supported")

# Get a list of all interfaces
interfaces = []
with os.popen("/sbin/ifconfig -a", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line[0] == '\t':
            continue
        if line[0] != ' ':
            interfaces.append(line.split()[0])

# Get a list of all interface indices
indices = []
with os.popen("/sbin/ifconfig -a", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line[0] == '\t':
            continue
        if line[
