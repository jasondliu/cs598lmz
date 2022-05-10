import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except OSError:
        pass
    else:
        assert False, 'Expected OSError'

def test_if_indextoname_2():
    try:
        socket.if_indextoname(1, 'foo')
    except OSError:
        pass
    else:
        assert False, 'Expected OSError'

def test_if_indextoname_3():
    try:
        socket.if_indextoname(1, 'foo', 'bar')
    except OSError:
        pass
    else:
        assert False, 'Expected OSError'

def test_if_indextoname_4():
    try:
        socket.if_indextoname(1, 'foo', 'bar', 'baz')
    except OSError:
        pass
    else:
        assert False, 'Expected OSError'

