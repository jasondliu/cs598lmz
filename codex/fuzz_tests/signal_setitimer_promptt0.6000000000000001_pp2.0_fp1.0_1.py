import signal
# Test signal.setitimer()
import os
import time
# Test os.times()
import mmap
# Test mmap.mmap()
import fcntl
# Test fcntl.fcntl()
import resource
# Test resource.getrlimit()
import socket
# Test socket.socketpair()
import sys
# Test sys.getcheckinterval()
import termios

try:
    import _thread
except ImportError:
    _thread = None

from test import support

# Test that the interpreter shutdown correctly with large recursive
# tuples, lists, dicts and sets.

def create_cycle(container, n):
    "Create an object with a reference cycle"
    lst = []
    for i in range(n):
        lst.append(container(lst))
    return lst[0]

def test_shutdown():
    # create_cycle() returns an object with a reference cycle.  The
    # cycle is eliminated during shutdown and the gc.collect()
    # call verifies that no objects are left behind.
    gc.collect()
    create_
