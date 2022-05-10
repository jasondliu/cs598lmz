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
    # The test also assumes that the loopback interface has index 1
    # and that eth0 has index 2.
    #
    # The test also assumes that the loopback interface has address
    # 127.0.0.1 and that eth0 has address 192.168.1.1.
    #
    # The test also assumes that the loopback interface has netmask
    # 255.0.0.0 and that eth0 has netmask 255.255.255.0.
    #
    # The test also assumes that the loopback interface has broadcast
    # address 127.255.255.255 and that eth0 has broadcast address
    # 192.168.1.255.

    # Test if_indextoname()
    assert socket.if_indextoname(1) == 'lo'
   
