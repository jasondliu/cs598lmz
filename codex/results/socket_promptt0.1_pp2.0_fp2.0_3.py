import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    ifname = socket.if_indextoname(1)
    if ifname is not None:
        print("if_indextoname(1) = %s" % ifname)
    else:
        print("if_indextoname(1) = None")

if __name__ == '__main__':
    test_if_indextoname()
