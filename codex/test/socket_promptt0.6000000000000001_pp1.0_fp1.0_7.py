import socket
# Test socket.if_indextoname and socket.if_nameindex

def test_if_nameindex():
    if_nameindex = socket.if_nameindex()
    if if_nameindex:
        if_nameindex = list(if_nameindex)
        for i in if_nameindex:
            if_name = socket.if_indextoname(i[0])
            assert if_name == i[1], \
                "if_indextoname(%s) == %s, wanted %s" % (i[0], if_name, i[1])
            assert socket.if_indextoname(i[0]) == i[1], \
                "if_indextoname(%s) == %s, wanted %s" % (i[0], if_name, i[1])
