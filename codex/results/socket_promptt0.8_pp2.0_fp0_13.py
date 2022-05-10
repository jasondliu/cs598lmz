import socket
# Test socket.if_indextoname

TEST_IFACE = "lo"
TEST_IFACE_IDX = 1

def test_if_indextoname():
    name = socket.if_indextoname(TEST_IFACE_IDX)
