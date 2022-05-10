import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

# This used to fail with a SystemError, because it would try to mutate
# the list while it was scanning it.
    select.select([F()], [], [])
    assert a == [1]

def test_select_large_fd():
    for fd in range(3, select.FD_SETSIZE + 2):
        try:
            f = open(str(fd), "wb")
        except OSError:
            break
        r, w, x = select.select([f], [], [], 0)
        assert r == [f]
        assert not w
        assert not x
