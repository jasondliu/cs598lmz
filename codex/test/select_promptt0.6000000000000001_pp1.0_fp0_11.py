import select
# Test select.select on a list of sockets.
# This test is not exhaustive.
import select
import socket
import time

def test(readable, writable, exceptable, timeout=None):
    readable, writable, exceptable = select.select(readable, writable,
                                                   exceptable, timeout)
