import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    f = F()
    s = select.select([f], [], [])
    assert not s[0]
    assert not s[1]
    assert not s[2]
    assert a == [1]

def test_select_closed_pipe():
    r, w = os.pipe()
    fd_count = len(select.select([r], [], []))
    os.close(w)
    assert fd_count == 1

    # calling select again should not segfault
    s = select.select([r], [], [])
    assert not s[0]
    assert not s[1]
    assert not s[2]
    os.close(r)

def test_select_closed_pipe_big():
    r, w = os.pipe()
    os.close(w)
    try:
        select.select([r], [], [], 0.1)
    except select.error as e:
        assert e[0] == errno.EBADF
