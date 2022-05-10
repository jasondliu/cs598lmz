import select
# Test select.select

def test_select():
    """
    >>> test_select()
    """
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    s.listen(1)
    port = s.getsockname()[1]
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("localhost", port))
    conn, addr = s.accept()
    c.send("hello")
    r, w, e = select.select([conn], [], [], 1)
    if r:
        assert conn.recv(1024) == "hello"
    else:
        assert 0, "timeout"
    c.close()
    conn.close()
    s.close()

def test_select_timeout():
    """
    >>> test_select_timeout()
    """
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
