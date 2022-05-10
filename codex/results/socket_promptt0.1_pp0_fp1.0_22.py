import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    #
    # This test is not very good, because it assumes that the first
    # interface is lo.  This is true on Linux, but not on other
    # platforms.  We should find a better way to test this.
    #
    # Also, we should test that if_indextoname() raises an exception
    # when passed an invalid index.
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo', 'if_indextoname() returned %s instead of lo' % ifname

def test_if_nameindex():
    # Test if_nameindex()
    #
    # This test is not very good, because it assumes that the first
    # interface is lo.  This is true on Linux, but not on other
    # platforms.  We should find a better way to test this.
    #
    # Also, we should test that if_nameindex() raises an exception
    # when passed an invalid index.
    if
