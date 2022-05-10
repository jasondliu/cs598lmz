import select
# Test select.select().

def test_select():
    from socket import socket, AF_INET, SOCK_DGRAM

    # Create two sockets.
    s1 = socket(AF_INET, SOCK_DGRAM)
    s2 = socket(AF_INET, SOCK_DGRAM)

    # Bind them to a localhost.
    s1.bind(('localhost', 0))
    s2.bind(('localhost', 0))

    # Send a message from one to the other.
    s1.sendto('hello', (s2.getsockname()))

    # Get the port number of s2.
    port = s2.getsockname()[1]

    # Use select to see if the message is readable.
    r, w, e = select.select([s2], [], [], 1)
    if r:
        data, addr = s2.recvfrom(1024)
        assert data == 'hello'

    # Make sure the port number is greater than 1024.
    assert port > 1024

    # Clean up.
    s1.close()
