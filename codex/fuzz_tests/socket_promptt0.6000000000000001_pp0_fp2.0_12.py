import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    if_nametoindex = socket.if_nametoindex
    ifname = if_indextoname(if_nametoindex("lo"))
    assert ifname == 'lo'
    try:
        if_indextoname(999)
    except ValueError:
        pass
    else:
        assert False, 'expected ValueError'
