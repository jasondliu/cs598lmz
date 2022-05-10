import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    s = select.select([F()], [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            del a[0]
            return len(a)

    s = select.select([F()], [], [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a[0:1] = [F()]
            return len(a)

    s = select.select([F()], [], [])

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            a.append(F())
            return len(a)

    s = select.select([F()], [], [])

def test_select_mutated5():
    a = []

    class F:
        def fileno(self):
            a.append(F())
            return len(a)

    class G:
        def
