import select
# Test select.select()

def test_select():
    import select
    import socket
    import time

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    port = s.getsockname()[1]
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect(('localhost', port))
    s3, addr = s.accept()

    # Test basic operation
    s.setblocking(0)
    s2.setblocking(0)
    s3.setblocking(0)
    for i in range(5):
        r, w, e = select.select([s], [s], [], 1.0)
        if (i & 1) == 0:
            assert r == [s]
            assert w == []
            assert e == []
        else:
            assert r == []
            assert w == [s]
            assert e == []
    s.close()
    s2
