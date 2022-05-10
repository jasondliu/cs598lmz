import socket
# Test socket.if_indextoname
if_indextoname = socket.if_indextoname

def test_if_indextoname():
    # Test if_indextoname with a valid interface index
    assert if_indextoname(1) == 'lo'

def test_if_indextoname_invalid():
    # Test if_indextoname with an invalid interface index
    raises(OSError, if_indextoname, -1)

def test_if_indextoname_exception():
    # Test if_indextoname with an invalid interface index
    raises(OSError, if_indextoname, -1)

# Test socket.if_nameindex
if_nameindex = socket.if_nameindex

def test_if_nameindex():
    # Test if_nameindex
    assert if_nameindex() == [ (1, 'lo') ]

# Test socket.if_nametoindex
if_nametoindex = socket.if_nametoindex

