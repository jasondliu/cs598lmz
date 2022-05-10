import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]
    f = F()
    a.append(f.fileno())

    select.select([f], [], [], 1)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            test_select_closed()
            return a[0]
        def close(self):
            a.pop()

    f = F()
    a.append(f.fileno())

    select.select([f], [], [], 1)

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_closed()
            return a[0]
        def close(self):
            a.pop()
            a.append(None)

    f = F()
    a.append(f.fileno())

    select.select([f], [], [], 1)
