import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)
    select.select([f], [], [], 0)
    a.pop()
    select.select([f], [], [], 0)

def test_select_error():
    a = []

    class F:
        def fileno(self):
            return 0
    f = F()
    a.append(f)
    select.select([f], [], [], 0)
    a.pop()
    raises(ValueError, select.select, [f], [], [], 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0
        def close(self):
            a.pop()
    f = F()
    a.append(f)
    select.select([f], [], [], 0)
    f.close()
    raises(ValueError, select.select, [f], [], [], 0)

def test_select_closed_mutated():
    a = []

