import socket
# Test socket.if_indextoname()
def test_if_indextoname():
    try:
        index = socket.if_nametoindex('lo')
    except:
        index = 1
    name = socket.if_indextoname(index)
    assert name == 'lo'

# Test socket.if_nameindex()
def test_if_nameindex():
    for if_index, if_name in socket.if_nameindex():
        break
    assert if_index == 1
    assert if_name == 'lo'

# Test socket.if_nametoindex()
def test_if_nametoindex():
    try:
        index = socket.if_nametoindex('lo')
    except:
        return
    assert index == 1
