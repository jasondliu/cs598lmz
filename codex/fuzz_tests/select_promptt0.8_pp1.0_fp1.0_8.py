import select
# Test select.select


def test_close():
    """
    Issue #1943: select.select() should not raise an exception
    if a file descriptor is closed in another thread while
    select() is blocking.
    """
    # Bind a socket to localhost:0, but don't accept any connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    port = s.getsockname()[1]

    # Start a thread that accepts a connection on that socket
    thread = threading.Thread(target=s.accept)
    thread.daemon = True
    thread.start()

    # Connect to the socket and close it immediately
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', port))
    client.close()

    # Wait for the thread to close the original socket
    thread.join()

    # Now try to run select.select() on the original socket
    # This used to raise
