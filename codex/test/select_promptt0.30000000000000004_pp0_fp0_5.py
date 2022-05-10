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
    conn.send(b'x' * 10)
    conn.close()
    s.close()
    assert select.select([conn], [], [], 0.0) == ([], [], [])

def test_select_large_list():
    # Issue #6106: select() shouldn't crash with a large list
    select.select([], range(10000), [])

