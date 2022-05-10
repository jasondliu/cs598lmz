import socket
# Test socket.if_indextoname()

def test_if_nameindex():
    l = socket.if_nameindex()
    if l:
        # just test it
        socket.if_indextoname(l[0][0])
        socket.if_nametoindex(l[0][1])

def test_if_nametoindex():
    socket.if_nametoindex('lo')

def test_if_indextoname():
    socket.if_indextoname(1)

def test_if_nameindex_exc():
    raises(socket.error, socket.if_nametoindex, 'nosuchnif')
    raises(socket.error, socket.if_indextoname, -1)

def test_if_nameindex():
    l = socket.if_nameindex()
    if l:
        # just test it
        socket.if_indextoname(l[0][0])
        socket.if_nametoindex(l[0][1])

def test_if_nameindex_exc():
    raises(socket.error, socket.
