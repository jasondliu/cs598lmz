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
    s2.send(b'x')
    time.sleep(0.1)
    r, w, e = select.select([s3], [], [], 1)
    if not (r, w, e) == ([s3], [], []):
        raise TestFailed("select returns %s, expected [%s] [] []" % (
            (r, w, e), s3))
    s3.close()
    s2.close()
    s.close()

def test_error():
    import select
    import socket

