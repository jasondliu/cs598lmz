import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    f = F()
    a.append(f.fileno())
    select.select([f], [], [])

def test_select_no_fd_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_no_fd_mutated()
            return a[0]

    f = F()
    a.append(f.fileno())
    select.select([f], [], [], 0)

def test_select_no_fd_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_no_fd_mutated_2()
            return a[0]

    f = F()
    a.append(f.fileno())
    select.select([f], [], [], 1)

def test_select_no_fd_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_no_fd_mutated_3()
