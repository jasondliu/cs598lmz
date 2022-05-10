import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    f.fileno()
    select.select([f], [], [], 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 0

    f = F()
    f.fileno()
    select.select([f], [], [], 0)

def test_select_closed_read():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 0
        def read(self, n):
            return b"x" * n

    f = F()
    f.fileno()
    select.select([f], [], [], 0)

def test_select_closed_write():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 0
        def write(self, s):
            return len(s)

    f = F()
    f.fileno()
    select.select
