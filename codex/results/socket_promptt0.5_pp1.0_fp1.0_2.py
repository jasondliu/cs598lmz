import socket
# Test socket.if_indextoname

if_indextoname = socket.if_indextoname

def test_basic():
    assert if_indextoname(1) == 'lo'
    assert if_indextoname(2) == 'eth0'

def test_invalid():
    raises(OSError, if_indextoname, -1)
    raises(OSError, if_indextoname, 0)
    raises(OSError, if_indextoname, 3)
    raises(OSError, if_indextoname, 4)
    raises(OSError, if_indextoname, 5)
    raises(OSError, if_indextoname, 6)

def test_non_numeric():
    raises(TypeError, if_indextoname, '1')

def test_non_integer():
    raises(TypeError, if_indextoname, 1.5)

def test_non_int():
    raises(TypeError, if_indextoname, None)
    raises(TypeError, if_indextoname,
