import socket
# Test socket.if_indextoname()
def test_socket_if_indextoname():
    name = socket.if_indextoname(1)
    print(name)
    assert(isinstance(name, str))

# Test socket.if_nameindex()
def test_socket_if_nameindex():
    if_list = socket.if_nameindex()
    #print(if_list)
    #print(len(if_list))
    assert(isinstance(if_list, list))

if __name__ == '__main__':
    test_socket_if_indextoname()
    test_socket_if_nameindex()
