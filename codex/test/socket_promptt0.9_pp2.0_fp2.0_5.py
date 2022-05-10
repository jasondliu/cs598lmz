import socket
# Test socket.if_indextoname() and socket.if_nameindex() against
# each other on the same platform.
# Each test returns a list of tuples of interface information.

def test_if_nameindex():
    names = socket.if_nameindex()
    assert names
    for name in names:
        assert len(name) == 2
        assert name[0] in [x[1][1] for x in socket.if_nametoindex(name[1])]
    index_map = dict(names)
    assert index_map
    for index, name in socket.if_indextoname.items():
        assert index == index_map[name]
        assert index in socket.if_nameindex()
    for index in index_map:
        assert index == socket.if_indextoname([index])
    for name in index_map:
        assert name == socket.if_indextoname[socket.if_nametoindex[name]]

def test_if_nametoindex():
    names = socket.if_nameindex()
    assert names
    assert socket.if_nameto
