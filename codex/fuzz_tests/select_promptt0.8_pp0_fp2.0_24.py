import select
# Test select.select with a file descriptor that is a large unsigned value.
import socket
import unittest
try:
    MAXFD = os.sysconf('SC_OPEN_MAX')
except (AttributeError, ValueError):
    MAXFD = 256
for fd in (MAXFD, MAXFD + 1000, MAXFD * 10):
    s = socket.fromfd(fd, socket.AF_INET, socket.SOCK_STREAM)
    try:
        read, write, exceptions = select.select([s], [], [])
        self.assertEqual(read, [s])
    except select.error as e:
        if e.args[0] == errno.EBADF:
            pass
        else:
            raise
    finally:
        os.close(fd)
