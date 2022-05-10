import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    assert raises(RuntimeError, select.select, [F()], [], [], 10)

def test_huge_struct():
    class F:
        def fileno(self):
            return 0
        def read(self, size):
            return 'a' * size
    bufsize = (2**14) + 1
    select.select([F()], [], [], 0)
    r = select.select([F()], [], [], 0, bufsize)
    assert r == ([F()], [], [])

def test_select_interruption():
    class F:
        def fileno(self):
            return 0
    l = [F()]
    select.select(l, l, l, 0)
    import signal
    signal.alarm(1)
    try:
        select.select(l, l, l, 60)
    except select.error, e:
        assert e.args == ('interrupted', 4)
    else:
        assert 0, "select.selec
