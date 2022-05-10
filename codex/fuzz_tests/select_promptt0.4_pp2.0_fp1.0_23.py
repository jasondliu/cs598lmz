import select
# Test select.select()

import socket

def test_select():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(1)
    s.setblocking(0)
    conn, addr = s.accept()
    conn.setblocking(0)
    #
    r, w, x = select.select([conn], [conn], [conn], 1.0)
    assert r == [conn]
    assert w == []
    assert x == []
    #
    r, w, x = select.select([conn], [conn], [conn], 1.0)
    assert r == []
    assert w == []
    assert x == []
    #
    r, w, x = select.select([conn], [conn], [conn], 1.0)
    assert r == []
    assert w == [conn]
    assert x == []
    #
    r, w, x = select.select([conn], [conn], [conn], 1.0)
