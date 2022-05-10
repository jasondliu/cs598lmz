import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname is not None:
        print("index 1: %s" % ifname)

if __name__ == '__main__':
    test_if_indextoname()
