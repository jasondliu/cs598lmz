import socket
# Test socket.if_indextoname
try:
    socket.if_indextoname(0)
except AttributeError:
    pass
else:
    import select


def test_select(sock1, sock2, sock3):
    r, w, e = select.select([sock1, sock2, sock3], [], [])
    assert r[0] == sock1 or r[0] == sock2 or r[0] == sock3
    assert r[1] == sock1 or r[1] == sock2 or r[1] == sock3
    assert r[2] == sock1 or r[2] == sock2 or r[2] == sock3
    assert len(r) == 3

    # select should take both bytes, str and unicode as first argument
    r, w, e = select.select(str(sock1), "", "")
    assert r == sock1.fileno()
    r, w, e = select.select(repr(sock1), "", "")
    assert r == sock1.fileno()
