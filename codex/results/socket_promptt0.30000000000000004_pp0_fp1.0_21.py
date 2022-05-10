import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    #
    # This test is not very useful, as it only tests if the function
    # returns a string.  It doesn't test if the string is a valid
    # interface name.
    #
    # The test is also not very portable, as it assumes that there is
    # at least one interface with an index of 1.
    #
    # It is better than nothing, though.
    try:
        socket.if_indextoname(1)
    except (AttributeError, socket.error):
        pass
    else:
        raise TestFailed("if_indextoname() didn't raise an exception")

if __name__ == "__main__":
    test_if_indextoname()
