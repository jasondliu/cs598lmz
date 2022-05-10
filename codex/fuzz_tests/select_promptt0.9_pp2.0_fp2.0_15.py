import select
# Test select.select on file descriptors

import support, time, socket

# Create sockets.
s1, s2 = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM)
s3, s4 = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM)

# Test "exceptional conditions" that no one cares about.
t, w, x = select.select([], [], [s2], 0)
t, w, x = select.select([], [], [s2])

# Create a file descriptor in read and write mode.
try:
    f = open(support.TESTFN, 'r+b')
except IOError, e:
    if e.errno != errno.EACCES: raise
    # Try reading and writing only.
    error = str(e)
    f = open(support.TESTFN, 'wb')
    f = open(support.TESTFN, 'rb')
else:
    error = "Opened file in read+write mode."

def cleanup_module():
    if
