import select
# Test select.select()

def test_select():
    # Test select() with a readable socket
    readable, _, _ = select.select([sock], [], [], 0)
    assert readable == [sock]
    # Test select() with a writable socket
    _, writable, _ = select.select([], [sock], [], 0)
    assert writable == [sock]
    # Test select() with an exceptional socket
    _, _, exceptional = select.select([], [], [sock], 0)
    assert exceptional == [sock]

# Test select.poll()

def test_poll():
    poll = select.poll()
    poll.register(sock, select.POLLIN)
    poll.register(sock, select.POLLOUT)
    poll.register(sock, select.POLLERR)
    # Test poll() with a readable socket
    readable = poll.poll(0)
    assert readable == [(sock.fileno(), select.POLLIN)]
    # Test poll() with a writable socket
    writable = poll
