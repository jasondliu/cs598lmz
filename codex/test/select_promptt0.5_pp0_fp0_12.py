import select
# Test select.select() with a list of sockets that is empty.
import socket
import sys
import time

def test_select_empty_list():
    start = time.time()
    # On Windows and Mac OS X, we get an empty list back immediately
    # with no error.
    # On Linux, we get an error.
    try:
        r, w, x = select.select([], [], [], 0.1)
    except ValueError:
        pass
    assert time.time() - start < 0.2

# On Windows, select() doesn't work on non-socket objects, even if
# they are file descriptors.
def test_select_socket_only():
    start = time.time()
    # On Windows and Mac OS X, we get an empty list back immediately
    # with no error.
    # On Linux, we get an error.
    try:
        r, w, x = select.select([sys.stdin], [], [], 0.1)
    except ValueError:
        pass
    assert time.time() - start < 0.2

# On
