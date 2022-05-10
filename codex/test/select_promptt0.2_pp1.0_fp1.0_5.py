import select
# Test select.select()

def test_select():
    import select
    import socket
    import time

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(1)
    port = s.getsockname()[1]
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect(('127.0.0.1', port))
    s3, addr = s.accept()
    s2.send(b'xxx')
    time.sleep(0.1)
    r, w, e = select.select([s3], [], [], 1)
    if s3 not in r:
        raise TestFailed("socket not ready for reading")
    if s3 in w or s3 in e:
        raise TestFailed("socket in wrong state")
    s3.recv(1)
    s3.close()
    s2.close()
    s.close()

