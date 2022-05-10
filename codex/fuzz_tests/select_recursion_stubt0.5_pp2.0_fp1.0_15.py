import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)
    try:
        select.select(a, a, a)
    except ValueError:
        pass

def test_select_bad_fd():
    a = []

    class F:
        def fileno(self):
            return -1

    f = F()
    a.append(f)
    try:
        select.select(a, a, a)
    except ValueError:
        pass

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return 1

    f = F()
    a.append(f)
    try:
        select.select(a, a, a)
    except ValueError:
        pass

def test_select_closed_fd_2():
    a = []

    class F:
        def fileno(self):
            return 2

    f = F()
    a.append(f)
    try:
        select.select(a, a, a)
   
