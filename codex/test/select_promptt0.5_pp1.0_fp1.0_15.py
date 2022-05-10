import select
# Test select.select() and select.poll()

def test_select():
    import select

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(0)
    s.bind(('127.0.0.1', 0))
    s.listen(1)
    port = s.getsockname()[1]

    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect(('127.0.0.1', port))

    s3, addr = s.accept()

    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4.connect(('127.0.0.1', port))

    for timeout in (0, 0.1):
        r, w, e = select.select([s, s2, s3], [], [], timeout)
        assert r == [s], r
