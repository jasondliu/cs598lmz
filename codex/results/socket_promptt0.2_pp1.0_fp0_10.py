import socket
# Test socket.if_indextoname()

import socket

def test_if_indextoname():
    # This test is only valid on Linux.
    if not hasattr(socket, "if_indextoname"):
        return
    # This test is only valid if there is at least one interface.
    if not socket.if_indextoname(1):
        return
    # This test is only valid if there is at least one interface with
    # an IPv4 address.
    try:
        socket.if_indextoname(1, socket.AF_INET)
    except OSError as e:
        if e.errno == 99:
            return
        raise
    # This test is only valid if there is at least one interface with
    # an IPv6 address.
    try:
        socket.if_indextoname(1, socket.AF_INET6)
    except OSError as e:
        if e.errno == 99:
            return
        raise
    # This test is only valid if there is at least one interface with
    # an IPv4 or
