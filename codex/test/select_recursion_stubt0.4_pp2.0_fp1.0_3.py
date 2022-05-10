import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1
    a.append(F())
    try:
        select.select([], [], a)
    except ValueError:
        pass

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return -1
    a.append(F())
    try:
        select.select([], [], a)
    except ValueError:
        pass

def test_select_closed_fd_2():
    a = []

    class F:
        def fileno(self):
            return -1
    a.append(F())
    try:
        select.select([], a, [])
    except ValueError:
        pass

def test_select_closed_fd_3():
    a = []

    class F:
        def fileno(self):
            return -1
    a.append(F())
    try:
        select.select(a, [], [])
    except ValueError:
        pass

