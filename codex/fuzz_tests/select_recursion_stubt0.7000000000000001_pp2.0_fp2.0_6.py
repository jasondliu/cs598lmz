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
    except IndexError:
        pass

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return len(a)

    a.append(F())
    a.append(F())
    a.append(F())
    a.append(F())
    a.append(F())
    del a[2]
    select.select(a, a, a)

def test_select_closed_fd_in_exception():
    a = []

    class F:
        def fileno(self):
            return len(a)

    a.append(F())
    a.append(F())
    a.append(F())

    try:
        raise IndexError
    except:
        del a[2]
        select.select(a, a, a)

def test_select_closed_fd_in_exception
