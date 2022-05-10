import select
# Test select.select()

def test_select():
    # Test basic operation
    r, w, x = select.select([], [], [], 0)
    assert len(r) == 0
    assert len(w) == 0
    assert len(x) == 0

    # Test that it works with a socket
    s = socket.socket()
    s.bind(('localhost', 0))
    s.listen(1)
    r, w, x = select.select([s], [], [], 0)
    assert len(r) == 1
    assert len(w) == 0
    assert len(x) == 0
    r, w, x = select.select([s], [], [], 0)
    assert len(r) == 0
    assert len(w) == 0
    assert len(x) == 0
    s.close()

    # Test that it works with a file
    f = open(TESTFN, 'w')
    r, w, x = select.select([f], [], [], 0)
    assert len(r) == 0
