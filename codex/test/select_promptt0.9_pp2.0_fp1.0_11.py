import select
# Test select.select
# Only works on unix
# Check the warning in docs: select.select(rlist, wlist, xlist[, timeout])
# > Under Windows, only sockets are supported; under other POSIX-compliant operating systems, all file descriptors can be used.
from socket import socket
s = socket()
s.bind(('127.0.0.1', 0))
s.listen(1)
try:
    r, w, e = select.select([s], [], [], 0)
except ValueError as e:
    if str(e) != 'file descriptor cannot be a negative integer (-1)':
        raise
try:
    r, w, e = select.select([], [s], [], 0)
except ValueError as e:
    if str(e) != 'file descriptor cannot be a negative integer (-1)':
        raise
try:
    r, w, e = select.select([], [], [s], 0)
except ValueError as e:
    if str(e) != 'file descriptor cannot be a negative integer (-1)':
        raise



