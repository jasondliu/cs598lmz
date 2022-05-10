import select
# Test select.select()

def test_select():
    """
    Test the select.select() function.
    """
    # Open a couple of sockets
    (s1, s2) = socket.socketpair()

    # Test reading
    for i in range(5):
        rfds, wfds, xfds = select.select([s1], [], [], 1.0)
