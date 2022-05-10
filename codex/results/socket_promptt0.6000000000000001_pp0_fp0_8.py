import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if socket.if_indextoname() works
    ifindex = socket.if_nametoindex("lo")
    ifname = socket.if_indextoname(ifindex)
    assert ifname == "lo", "if_indextoname() failed"
