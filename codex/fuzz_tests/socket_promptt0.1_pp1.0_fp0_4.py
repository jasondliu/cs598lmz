import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    #
    # This test is Linux specific.
    #
    # The test assumes that the loopback interface is lo and that
    # there is an interface called eth0.
    #
    # The test also assumes that the index of lo is 1 and that the
    # index of eth0 is 2.
    #
    # If the test fails, the test will print the name of the loopback
    # interface and the name of the interface with index 2.
    #
    # If the test fails, the test will also print the index of lo and
    # the index of eth0.
    #
    # If the test fails, the test will also print the value of
    # socket.if_nametoindex('lo') and the value of
    # socket.if_nametoindex('eth0').
    #
    # If the test fails, the test will also print the value of
    # socket.if_indextoname(1) and the value of socket.if_indextoname
