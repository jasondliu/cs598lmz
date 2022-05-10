import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [])
    a.append(1)
    assert a

def test_select_blocking():
    import select
    import socket
    import os
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(1)
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(s.getsockname())
    r, w, e = select.select([c], [], [], None)
    assert r == [c]
    assert w == []
    assert e == []

    os.write(c.fileno(), b'x')
    r, w, e = select.select([s], [], [], None)
    assert r == [s]
    assert w == []
    assert e == []
    s.close()
    c.close()

def test_select_blocking_errnos():
   
