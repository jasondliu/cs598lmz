import socket
# Test socket.if_indextoname()
if_indextoname = socket.if_indextoname

def test_if_indextoname():
    # Test if_indextoname()
    #
    # This test is Linux specific.
    #
    # The test assumes that the loopback interface is present and
    # has index 1.
    #
    # The test also assumes that the first non-loopback interface
    # has index 2.
    #
    # The test also assumes that the interface name for the first
    # non-loopback interface is at least 3 characters long.

    # Get the name of the first non-loopback interface
    try:
        name = if_indextoname(2)
    except ValueError:
        raise unittest.SkipTest("no non-loopback interfaces")
    if len(name) < 3:
        raise unittest.SkipTest("interface name too short")

    # Check that the loopback interface has index 1
    index = socket.if_nametoindex("lo")
    if index != 1:
        raise unittest.SkipTest("
