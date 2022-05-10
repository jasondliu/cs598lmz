import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    def g():
        a.append(1)
        return [F()]

    r, w, x = select.select([], [], [], 1, g)
    assert r == []
    assert w == []
    assert x == []
    assert a == [], "select() mutated the contents of the fd lists"

def test_select_fileobj():
    def fileno(self):
        return self.fd

    def close(self):
        self.closed = True

    a = []
    class F:
        closed = False
        fd = -1
        fileno = fileno
        close = close

    f = F()
    f.fd = os.pipe()[0]

    select.select([f], [], [], 1)
    assert not f.closed

    select.select([], [f], [], 1)
    assert not f.closed

    select.select([], [], [f], 1)
    assert not f.closed

    f.close()
    assert f.closed

def test_select
