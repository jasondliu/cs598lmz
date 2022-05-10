import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    ifname = socket.if_indextoname(1)
    if ifname != 'lo':
        raise TestFailed('if_indextoname(1) returned %s instead of lo' % ifname)

    # Test if_indextoname() with invalid index
    try:
        socket.if_indextoname(-1)
    except ValueError:
        pass
    else:
        raise TestFailed('if_indextoname(-1) did not raise ValueError')

# Test socket.if_nameindex()

def test_if_nameindex():
    # Test if_nameindex()
    nameindex = socket.if_nameindex()
    if len(nameindex) == 0:
        raise TestFailed('if_nameindex() returned empty list')
    for i in range(len(nameindex)):
        ifname = socket.if_indextoname(nameindex[i][0])
