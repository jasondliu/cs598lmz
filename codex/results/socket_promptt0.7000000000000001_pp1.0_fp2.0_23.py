import socket
# Test socket.if_indextoname

def test_socket_if_indextoname():
    # Test if_indextoname
    # XXX(nnorwitz): should we change the if name to make this more portable?
    socket.if_indextoname(socket.if_nametoindex('lo'))

# Test socket.if_nameindex

def test_socket_if_nameindex():
    # Test if_nameindex
    for index, name in socket.if_nameindex():
        socket.if_indextoname(index)
        socket.if_nametoindex(name)

def test_socket_if_nameindex_negative():
    # Test if_nameindex
    for index, name in socket.if_nameindex():
        if index == 0:
            continue
        try:
            socket.if_indextoname(-index)
        except ValueError:
            pass
        else:
            raise AssertionError("negative index should fail")

# Test socket.if_nametoindex

def test_socket_if_nametoindex():
    # Test if_
