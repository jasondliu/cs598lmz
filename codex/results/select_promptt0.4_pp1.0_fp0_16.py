import select
# Test select.select()

def test_select():
    import _socket
    s = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(5)
    port = s.getsockname()[1]
    s2 = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    s2.connect(('localhost', port))
    s3, addr = s.accept()
    s4 = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    s4.connect(('localhost', port))
    s5, addr = s.accept()
    s6 = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    s6.connect(('localhost', port))
    s7, addr = s.accept()
    s8 = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    s8.connect(('localhost', port
