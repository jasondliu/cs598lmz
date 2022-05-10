import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    a.append(F())
    # Crash 
    select.select([], a, [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1
    a.append(F())
    # Crash 
    select.select([], a, [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a[:] = []
            return 1
    a.append(F())
    # Crash 
    select.select([], a, [])

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            a[:] = [1]
            return 1
    a.append(F())
    # Crash 
    select.select([], a, [])


def test_select_mutated5():
    a = []

    class F:
        def fileno(self):
            a
