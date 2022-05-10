import select
# Test select.select()
import socket

def test_select():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(1)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect(s.getsockname())
    s3, addr = s.accept()
    s3.send(b"x")
    s2.send(b"x")
    s2.close()
    s3.close()
    s.close()
    assert select.select([s2], [], [], 0) == ([], [], [])
    assert select.select([s3], [], [], 0) == ([], [], [])
    assert select.select([s], [], [], 0) == ([], [], [])

def test_select_error():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind
