import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return f.fileno()

    f = F()
    a.append(f)
    a.remove(f)
    select.select([f], [], [])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return f.fileno()

    f = F()
    a.append(f)
    a.remove(f)
    del f
    select.select([f], [], [])

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            test_select_closed_fd()
            return fd

    f = F()
    a.append(f)
    a.remove(f)
    fd = f.fileno()
    del f
    select.select([f], [], [])

def test_select_closed_fd_2():
    a = []

    class F:
        def fileno(self):
            return fd

    f = F()
    a.append(
