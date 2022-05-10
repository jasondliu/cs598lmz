import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()
    a.append(f)
    select.select([f], [f], [f])

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            test_select_closed_fd()
            return len(a)
    f = F()
    a.append(f)
    select.select([f], [f], [f])

def test_select_closed_fd_2():
    a = []

    class F:
        def fileno(self):
            test_select_closed_fd_2()
            return len(a)
    f = F()
    a.append(f)
    select.select([f], [f], [f])

def test_select_closed_fd_3():
    a = []

    class F:
        def fileno(self):
            test_select_closed_fd_3()
            return len(a)
    f = F()
    a.append(f)
