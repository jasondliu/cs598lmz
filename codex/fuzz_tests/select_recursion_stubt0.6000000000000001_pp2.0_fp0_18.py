import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 3

    select.select([F()], [], [], 0)

def test_select_closed_after():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 3

    select.select([F()], [F()], [], 0)

def test_select_bad_fd():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_bad_fd_after():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    select.select([F()], [F()], [], 0)

def test_select_bad_fd_2():
    a = []


