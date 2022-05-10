import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # test with an invalid index
    invalid = 999
    try:
        socket.if_indextoname(invalid)
    except socket.error as e:
        if e.errno == errno.ENXIO:
            pass
        else:
            raise
    else:
        raise Exception("socket.if_indextoname(%d) succeeded" % (invalid,))

    # test with a valid index
    valid = socket.if_nametoindex('lo')
    name = socket.if_indextoname(valid)
    assert name == 'lo', name

    # test with a valid interface name
    valid = 'lo'
    index = socket.if_nametoindex(valid)
    name = socket.if_indextoname(index)
    assert name == 'lo', name

    # test with a valid interface name
    valid = 'lo'
    index = socket.if_nametoindex(valid)
    name = socket.if_indextoname(index)
    assert
