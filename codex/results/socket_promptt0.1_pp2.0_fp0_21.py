import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    #
    # This test is Linux specific.
    #
    # The test assumes that the system has at least one network interface
    # and that the first one is named "lo".
    #
    # The test also assumes that the system has at least one other network
    # interface.
    #
    # The test also assumes that the system has at least one network
    # interface that is not named "lo".
    #
    # The test also assumes that the system has at least one network
    # interface that is not named "lo" and that is not named "eth0".
    #
    # The test also assumes that the system has at least one network
    # interface that is not named "lo" and that is not named "eth0" and
    # that is not named "wlan0".
    #
    # The test also assumes that the system has at least one network
    # interface that is not named "lo" and that is not named "eth0" and
    # that is not named
