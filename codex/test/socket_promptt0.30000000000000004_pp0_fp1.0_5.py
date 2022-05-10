import socket
# Test socket.if_indextoname()

def test_if_indextoname(dev, family):
    try:
        socket.if_indextoname(1)
    except OSError as e:
        if e.errno == errno.EINVAL:
            print('if_indextoname(1) failed with EINVAL')
        else:
            print('if_indextoname(1) failed with %d' % e.errno)
    else:
        print('if_indextoname(1) succeeded')

# Test socket.if_nameindex()

def test_if_nameindex():
    try:
        socket.if_nameindex()
    except OSError as e:
        if e.errno == errno.EINVAL:
            print('if_nameindex() failed with EINVAL')
        else:
            print('if_nameindex() failed with %d' % e.errno)
    else:
        print('if_nameindex() succeeded')

# Test socket.if_nametoindex()

