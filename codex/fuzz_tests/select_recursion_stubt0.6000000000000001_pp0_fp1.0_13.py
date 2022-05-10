import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    select.select([], [], a)


def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(0)
            return 0

    a.append(F())
    select.select([], [], a)


def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.append(0)
            return 0

    a.append(F())
    select.select([], a, a)


def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            a.append(0)
            return 0

    a.append(F())
    select.select(a, a, a)


def test_select_mutated5():
    a = []

    class F:
        def fileno(self):
            a.append(0)
            return 0

    a.append(F())
   
