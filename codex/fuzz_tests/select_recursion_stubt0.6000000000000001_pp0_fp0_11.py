import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())
    a.append(F())

    try:
        select.select(a, a, a)
    except RuntimeError:
        # this is the expected outcome
        return
    raise Exception("Expected RuntimeError!")

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(None)
            return 1
    a.append(F())
    a.append(F())

    select.select(a, a, a)

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.append(None)
            return 1
    a.append(F())
    a.append(F())

    select.select(a, a, a, 1)

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            del a[:]
            return 1
    a.append(F())
    a.append(F())
