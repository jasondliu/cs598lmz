import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
        def close(self):
            a.append(1)
    f = F()
    fd = f.fileno()

    try:
        select.select([], [], [f])
    except ValueError:
        pass
    else:
        assert False, "Didn't raise ValueError"
    assert a == [1], a

def test_select_error():
    import _socket
    s = _socket.socket()
    l = []
    try:
        select.select([s], [s], [s])
    except select.error as e:
        l = list(e.args)
    assert l[0] == errno.EBADF, l

def test_select_keyboardinterrupt():
    l = []
    try:
        select.select([], [], [], 0)
    except KeyboardInterrupt as e:
        l = list(e.args)
    assert l == [], l

def test_select_keyboardinterrupt_timeout():
    import time
