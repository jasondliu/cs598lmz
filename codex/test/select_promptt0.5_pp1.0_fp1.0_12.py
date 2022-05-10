import select
# Test select.select() with a large number of file descriptors.

import os
import select
import socket
import subprocess
import sys
import time

# This is a list of file descriptors that we will pass to select.select().
# Each file descriptor is created by a different method, to ensure that
# select.select() can handle all types of file descriptors.
fds = []

# Create a pipe and add both ends to the list.
r, w = os.pipe()
fds.append(r)
fds.append(w)

# Create a socket and add it to the list.
s = socket.socket()
s.bind(('', 0))
s.listen(1)
fds.append(s)

# Create a pty and add both ends to the list.
m, s = os.openpty()
fds.append(m)
fds.append(s)

# Create a subprocess with both stdin and stdout connected to pipes, and add
# both of the pipes to the list.
