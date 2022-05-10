import select
# Test select.select()

def test_select():
    import _socket
    s = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    s.listen(1)
    s2, addr = s.accept()
    s2.close()
    s.close()

def test_poll():
    import _socket
    s = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    s.listen(1)
    s2, addr = s.accept()
    s2.close()
    s.close()

def test_epoll():
    import _socket
    s = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    s.listen(1)
    s2, addr = s.accept()
