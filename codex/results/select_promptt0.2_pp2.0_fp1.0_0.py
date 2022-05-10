import select
# Test select.select()

def test_select():
    import select
    import socket
    import time

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    s.listen(1)
    s.setblocking(0)
    port = s.getsockname()[1]
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect(("127.0.0.1", port))
    s3, addr = s.accept()
    s2.setblocking(0)
    s3.setblocking(0)

    # Test basic operation
    r, w, x = select.select([s2], [s3], [])
    assert r == [s2]
    assert w == [s3]
    assert x == []

    # Test modifying the returned lists
    r, w, x = select.select([s2], [s3], [])
    del r[0]
    del w
