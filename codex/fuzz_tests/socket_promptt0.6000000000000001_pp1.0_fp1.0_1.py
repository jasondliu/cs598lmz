import socket
# Test socket.if_indextoname()
def test_if_indextoname():
    print(socket.if_indextoname(1))
    return

# Test socket.if_nameindex()
def test_if_nameindex():
    print(socket.if_nameindex())
    return

# Test socket.if_nametoindex()
def test_if_nametoindex():
    print(socket.if_nametoindex('eth0'))
    return

def main():
    test_if_indextoname()
    test_if_nameindex()
    test_if_nametoindex()
    return

if __name__ == '__main__':
    main()
