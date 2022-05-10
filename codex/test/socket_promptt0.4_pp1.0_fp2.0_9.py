import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname is None:
        print('if_indextoname() failed')
        return
    print('if_indextoname(1) =', ifname)

test_if_indextoname()
