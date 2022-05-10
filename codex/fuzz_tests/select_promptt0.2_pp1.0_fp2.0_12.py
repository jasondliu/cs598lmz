import select
# Test select.select()

def test_select():
    import select
    import socket
    import time
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(1)
    s2, addr = s.accept()
    s.close()
    s2.setblocking(0)
    s2.send(b'x')
    time.sleep(0.1)
    r, w, e = select.select([s2], [], [], 0.1)
    assert r == [s2]
    s2.close()

def test_select_timeout():
    import select
    import socket
    import time
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(1)
    s2, addr = s.accept()
    s.close()
    s2.setblocking(0)
   
