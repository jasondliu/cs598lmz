import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    a.append(F())
    a.append(F())
    try:
        select.select(a, a, a)
    except RuntimeError:
        pass

def test_select_closed():
    class F:
        def fileno(self):
            return 3

    a = [F()]
    try:
        select.select([a], [a], [a])
    except RuntimeError:
        pass

def test_select_regression():
    try:
        fd, tmpfile = tempfile.mkstemp()
        os.close(fd)
        l = [open(tmpfile)]
        r, w, x = select.select([], l, [])
        assert l == w
        os.remove(tmpfile)
    except OSError:
        pass
