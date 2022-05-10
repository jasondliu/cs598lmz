import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Check that if_indextoname() returns the correct interface name
    # for a given index.
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_indextoname_invalid():
    # Check that if_indextoname() raises an exception for an invalid
    # interface index.
    raises(OSError, socket.if_indextoname, -1)

def test_if_indextoname_null():
    # Check that if_indextoname() returns None for an index of 0.
    assert socket.if_indextoname(0) is None

def test_if_indextoname_non_integer():
    # Check that if_indextoname() raises a TypeError for a non-integer
    # index.
    raises(TypeError, socket.if_indextoname, '1')

def test_if_indextoname_overflow():
    # Check that if_ind
