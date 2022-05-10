import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def close(self):
            a.pop()

    a.append(F())
    select.select([], [], [])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            test_select_closed()
            return len(a)
        def close(self):
            a.pop()

    a.append(F())
    select.select([], [], [], 0.1)
    a[0].close()
    select.select([], [], [], 0.1)
