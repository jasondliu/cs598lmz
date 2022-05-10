import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5

    a.append(F())
    select.select([], a, [])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 5

    f = F()
    a.append(f)
    del f
    select.select([], a, [])

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return 5

    f = F()
    a.append(f)
    f.close = lambda : 5
    del f
    select.select([], a, [])

def test_select_closed_fd_2():
    a = []

    class F:
        def fileno(self):
            return 5

    f = F()
    a.append(f)
    f.close = lambda : 5
    select.select([], a, [])
    del f

def test_select_closed_fd_3():
    a = []

