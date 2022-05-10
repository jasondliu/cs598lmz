import socket
# Test socket.if_indextoname() function

def test_ifindex_get(index):
    """Return the name of a network interface, given the index."""
    try:
        return socket.if_indextoname(index)
    except (OSError, ValueError):
        return None

test_ifindex_get(1)
test_ifindex_get(2)
test_ifindex_get(3)
test_ifindex_get(4)
test_ifindex_get(5)
test_ifindex_get(20)
test_ifindex_get(30)
test_ifindex_get(33)
test_ifindex_get(12)
test_ifindex_get(15)
test_ifindex_get(16)
test_ifindex_get(17)
test_ifindex_get(18)
