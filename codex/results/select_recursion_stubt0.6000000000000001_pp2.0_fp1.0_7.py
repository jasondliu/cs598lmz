import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 3

    s = select.select([F()], [], [], 0)
    assert s == ([3], [], [])
    assert a == [1]

def test_select_bug():
    # test that we don't crash when calling fileno before select
    class F:
        def fileno(self):
            return 3

    f = F()
    f.fileno()
    s = select.select([f], [], [], 0)
    assert s == ([3], [], [])

def test_select_closed_pipe():
    fd_r, fd_w = os.pipe()
    try:
        os.close(fd_w)
        fd_w = None
        fd_r = os.fdopen(fd_r, 'rb')
        fd_r.fileno()
        fd_r.read()
        s = select.select([fd_r], [], [], 0)
        assert s == ([], [], [])
    finally:
        if f
