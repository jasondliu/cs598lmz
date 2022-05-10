import socket
# Test socket.if_indextoname and socket.if_nametoindex
def test_if_indextoname(ifname):
    """Test socket.if_indextoname"""
    try:
        ifidx = socket.if_nametoindex(ifname)
    except (AttributeError, socket.error):
        try:
            ifidx = socket.if_nametoindex(ifname.encode('ascii'))
        except (AttributeError, socket.error):
            print('socket.if_nametoindex is not available')
            return
    try:
        iname = socket.if_indextoname(ifidx)
    except (AttributeError, socket.error):
        try:
            iname = socket.if_indextoname(ifidx).decode('ascii')
        except (AttributeError, socket.error):
            print('socket.if_indextoname is not available')
            return
    print('%d <-> %s' % (ifidx, iname))
    if ifname != iname:
        print('ERROR: if_nam
