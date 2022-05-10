import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()
    fd = f.fileno()
    a.append(f)
    s = select.select([f], [], [])
    assert s == ([f], [], [])
    assert a == [f]

def test_select_read_mutation():
    import select
    a = []
    class F:
        def fileno(self):
            return len(a)
    f = F()
    fd = f.fileno()
    a.append(f)
    read, _, _ = select.select([f], [], [], 0)
    assert read == [f], "expected [f], got %r" % (read,)

def test_select_write_mutation():
    import select
    a = []
    class F:
        def fileno(self):
            return len(a)
    f = F()
    fd = f.fileno()
    a.append(f)
    _, write, _ = select.select([], [f], [], 0
