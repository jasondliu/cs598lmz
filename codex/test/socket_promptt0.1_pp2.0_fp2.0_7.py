import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Check that if_indextoname() returns a string
    assert isinstance(socket.if_indextoname(1), str)

def test_if_indextoname_error():
    # Check that if_indextoname() raises an exception for invalid index
    raises(OSError, socket.if_indextoname, -1)
    raises(OSError, socket.if_indextoname, 0)

def test_if_indextoname_non_integer():
    # Check that if_indextoname() raises an exception for non-integer index
    raises(TypeError, socket.if_indextoname, None)
    raises(TypeError, socket.if_indextoname, "1")

def test_if_indextoname_non_integer_index():
    # Check that if_indextoname() raises an exception for non-integer index
    raises(TypeError, socket.if_indextoname, 1.1)

