import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    f = F()
    a.append(f)
    select.select([f], [], [])

def test_select_fd_disappeared():
    a = []

    class F:
        def fileno(self):
            return a[0]

    f = F()
    a.append(f)
    a.pop()
    select.select([f], [], [])

def test_select_fd_disappeared_2():
    a = []

    class F:
        def fileno(self):
            return a[0]

    f = F()
    a.append(f)
    a.pop()
    try:
        select.select([f], [], [])
    except ValueError:
        pass
    else:
        assert False, "should have raised"

def test_select_fd_disappeared_3():
    a = []

    class F:
        def fileno(self):
            return a[0]

    f = F()
