import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    #
    # This test is Linux specific.
    #
    # The test assumes that the loopback interface is named 'lo' and that
    # the first non-loopback interface is named 'eth0'.
    #
    # The test also assumes that the loopback interface has index 1 and
    # that the first non-loopback interface has index 2.
    #
    # If the test fails, the error message will indicate the name of the
    # loopback interface and the name of the first non-loopback interface.
    #
    # If the test fails, the error message will also indicate the index
    # of the loopback interface and the index of the first non-loopback
    # interface.
    #
    # If the test fails, the error message will also indicate the name
    # of the interface with index 1 and the name of the interface with
    # index 2.
    #
    # If the test fails, the error message will also indicate the index
    # of the interface named '
