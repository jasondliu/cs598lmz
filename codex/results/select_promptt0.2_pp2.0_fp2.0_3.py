import select
# Test select.select()

def test_select():
    import select
    import socket
    import time
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    s.listen(1)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect(s.getsockname())
    s3, addr = s.accept()
    s2.send(b"x")
    time.sleep(1)
    r, w, x = select.select([s3], [], [], 0)
    assert r == [s3]
    s3.recv(1)
    s3.close()
    s2.close()
    s.close()

def test_select_large_list():
    import select
    import socket
    import time
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.
