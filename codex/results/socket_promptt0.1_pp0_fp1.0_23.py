import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    ifname = socket.if_indextoname(1)
    if not ifname:
        raise TestFailed, "Could not find interface 1"
    if socket.if_indextoname(1) != ifname:
        raise TestFailed, "if_indextoname() returned different names for the same index"
    if socket.if_indextoname(2) == ifname:
        raise TestFailed, "if_indextoname() returned the same name for different indices"
    if socket.if_indextoname(1000000000) != None:
        raise TestFailed, "if_indextoname() returned a name for an invalid index"

test_if_indextoname()
