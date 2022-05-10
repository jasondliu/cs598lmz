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
        print rfds
        assert rfds == [s1]
        s2.send(b'x')
        assert s1.recv(1) == b'x'

    # Test writing
    for i in range(5):
        rfds, wfds, xfds = select.select([], [s2], [], 1.0)
        print wfds
        assert wfds == [s2]
        s1.send(b'x')
        assert s2.recv(1) == b'x'

    # Test exceptions
    for i in range(5):
        rfds, wfds, xfds = select.select([], [
