import socket
# Test socket.if_indextoname() and socket.if_nameindex()

def if_indextoname(index):
    try:
        return socket.if_indextoname(index)
    except ValueError:
        return None

def if_nameindex():
    return [ (index, socket.if_indextoname(index))
             for index in socket.if_nameindex() ]

def test_if_nameindex():
    # Check that all results can be converted back to their index
    for index, name in if_nameindex():
        if if_indextoname(index) != name:
            print('if_indextoname(%d) is %r, should be %r' % (index,
                  if_indextoname(index), name))

