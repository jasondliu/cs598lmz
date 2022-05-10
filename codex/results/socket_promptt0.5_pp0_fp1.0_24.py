import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    # If this test fails, it is likely that the host has no interfaces
    # defined.
    ifname = socket.if_indextoname(1)
    if ifname != "lo":
        raise TestFailed, "if_indextoname(1) returned %s instead of 'lo'" % ifname

if __name__ == "__main__":
    test_if_indextoname()
