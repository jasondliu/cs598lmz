import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()
    a.append(f)
    try:
        select.select([f], [f], [f], 0)
    except ValueError:
        pass
    else:
        raise Exception("did not detect mutated list")

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return len(a)
    f = F()
    a.append(f)
    del a[:]
    try:
        select.select([f], [f], [f], 0)
    except ValueError:
        pass
    else:
        raise Exception("did not detect closed list")

def test_select_closed_fd():
    import os
    a = []

    class F:
        def fileno(self):
            return len(a)
    f = F()
    a.append(f)
    os.close(f.fileno())
