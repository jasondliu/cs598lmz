import select
# Test select.select() using select() system call on non-blocking sockets.
# The first argument to select() is the list of sockets to be checked, the
# second is the list of sockets with data available for reading, and the
# third is the list of sockets ready for writing.  The lists are updated
# to only include the sockets that actually changed state, and an optional
# 4th argument gives a timeout in seconds.

# This is a test and example program.  It is expected to run forever.

import os
import sys
import time

MSG = b"This is a test.  This is only a test.\r\n"


def reader(s):
    try:
        while 1:
            buf = s.recv(1024)
            if not buf:
                raise RuntimeError("Connection closed")
            sys.stdout.buffer.write(buf)
            sys.stdout.flush()
    except KeyboardInterrupt:
        pass


def writer(s):
    for i in range(1000):
        time.sleep(0.1)
        s.send(MSG)
