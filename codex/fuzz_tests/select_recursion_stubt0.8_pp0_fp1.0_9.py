import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
        def read(self, size):
            a.append(1)
            raise OSError()

    t = select.select([F()], [], [], timeout=0.1)
    raises(OSError, len, t)
    assert len(a) == 1

def test_select_fd_mutated():
    a = []
    class F:
        def read(self, size):
            a.append(1)
            raise OSError()

    f = F()
    assert select.select([f], [], [], timeout=0.1) == ([f], [], [])
    assert len(a) == 1
    assert f.closed == False
    raises(OSError, select.select, [f], [], [], timeout=0.1)
    assert f.closed == True
    assert len(a) == 2
    raises(OSError, select.select, [f], [], [], timeout=0.1)
    assert len(a) == 2
