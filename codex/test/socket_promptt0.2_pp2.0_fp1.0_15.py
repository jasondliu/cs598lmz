import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    #
    # This test is Linux-specific.  It assumes that the loopback interface
    # has index 1 and the first Ethernet interface has index 2.

    if_indextoname = socket.if_indextoname
    if_nametoindex = socket.if_nametoindex

    assert if_indextoname(1) == 'lo'
    assert if_indextoname(2) == 'eth0'
    assert if_nametoindex('lo') == 1
    assert if_nametoindex('eth0') == 2
    raises(OSError, if_indextoname, 0)
    raises(OSError, if_indextoname, -1)
    raises(OSError, if_indextoname, 3)
    raises(OSError, if_nametoindex, 'nosuchinterface')
    raises(OSError, if_nametoindex, '')
    raises(TypeError, if_indextoname, '1')
