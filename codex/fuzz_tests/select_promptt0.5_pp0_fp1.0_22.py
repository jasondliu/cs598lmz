import select
# Test select.select function

def test_select():
    # Create a pair of connected sockets
    # to test select()
    (server, client) = socket.socketpair()

    # Send data from client to server
    client.send(b'x')
    assert server.recv(100) == b'x'

    # Send data from server to client
    server.send(b'y')
    assert client.recv(100) == b'y'

    # Test that select() works
    readable, writable, exceptional = select.select([server], [], [], 1.0)
    assert readable == [server]

    # Test that select() works with a timeout
    readable, writable, exceptional = select.select([server], [], [], 0.1)
    assert readable == []

    # Test that select() works with a closed socket
    server.close()
    readable, writable, exceptional = select.select([server], [], [], 1.0)
    assert readable == []
