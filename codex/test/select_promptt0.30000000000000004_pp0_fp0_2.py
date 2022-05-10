import select
# Test select.select()

def test_select():
    import time
    import select

    # Test basic operation
    r, w, x = select.select([], [], [], 0.1)
    assert len(r) == len(w) == len(x) == 0

    # Test that it works with a file
    f = open(__file__, 'rb')
    try:
        r, w, x = select.select([f], [], [], 0.1)
        assert not r and not w and not x
    finally:
        f.close()

    # Test that it works with an invalid fd
    r, w, x = select.select([-1], [], [], 0.1)
    assert not r and not w and not x

    # Test that it works with a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(False)
    s.bind(('localhost', 0))
    s.listen(1)
