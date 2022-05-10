import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    print('testing if_indextoname()')
    print(socket.if_indextoname(1))
    print(socket.if_indextoname(0))

def test_if_nameindex():
    print('testing if_nameindex()')
    print(socket.if_nameindex())

def test_if_nametoindex():
    print('testing if_nametoindex()')
    print(socket.if_nametoindex('lo'))
    print(socket.if_nametoindex('eth0'))

#test_if_indextoname()
#test_if_nametoindex()
test_if_nameindex()
