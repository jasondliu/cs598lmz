import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    print(ifname)

if __name__ == '__main__':
    test_if_indextoname()
