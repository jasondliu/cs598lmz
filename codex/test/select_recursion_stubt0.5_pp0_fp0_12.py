import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def close(self):
            a.append(1)

    f = F()
    select.select([f], [], [], 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return len(a)
        def close(self):
            a.append(1)

    f = F()
    f.close()
    select.select([f], [], [], 0)

def test_select_mutated_closed():
    a = []

    class F:
        def fileno(self):
            f.close()
            return len(a)
        def close(self):
            a.append(1)

    f = F()
    select.select([f], [], [], 0)
