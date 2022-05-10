import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    #
    # This test is Linux specific.
    #
    # The test assumes that the system has at least one network interface
    # and that the first network interface has an index of 1.
    #
    # The test also assumes that the first network interface is not
    # a loopback interface.
    #
    # The test also assumes that the first network interface is not
    # a point-to-point interface.
    #
    # The test also assumes that the first network interface is not
    # a virtual interface.
    #
    # The test also assumes that the first network interface is not
    # a tunnel interface.
    #
    # The test also assumes that the first network interface is not
    # a bridge interface.
    #
    # The test also assumes that the first network interface is not
    # a bonding interface.
    #
    # The test also assumes that the first network interface is not
    # a VLAN interface.
    #
    # The test also assumes that the
