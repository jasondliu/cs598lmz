import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    select.select([F()], [], [], 0)

def test_select_fd_mutated():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 0
    select.select([F()], [], [], 0)

def test_select_fd_mutated_2():
    a = []

    class F:
        def fileno(self):
            a[0] = 1
            return 0
    select.select([F()], [], [], 0)

class F:
    def fileno(self):
        return 0

def test_select_fd_mutated_3():
    f = F()
    f.fileno = lambda: 1
    select.select([f], [], [], 0)

def test_select_fd_mutated_4():
    f = F()
    f.fileno = lambda: 1
    select.select([f], [], [], 0)

