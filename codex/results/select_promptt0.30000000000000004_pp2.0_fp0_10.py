import select
# Test select.select()

def test_select():
    import select
    import socket
    import time

    # Create two sockets
    s1 = socket.socket()
    s2 = socket.socket()

    # Bind them to localhost on arbitrary port numbers
    s1.bind(('localhost', 0))
    s2.bind(('localhost', 0))

    # Get the port numbers
    s1.listen(1)
    s2.listen(1)
    port1 = s1.getsockname()[1]
    port2 = s2.getsockname()[1]
    s1.close()
    s2.close()

    # Connect s1 to s2 and vice versa
    s1 = socket.socket()
    s2 = socket.socket()
    s1.connect(('localhost', port2))
    s2.connect(('localhost', port1))

    # Wait for a bit
    time.sleep(1)

    # Both sockets should be writable
    r, w, e = select.select([], [s1, s2], [], 0)
