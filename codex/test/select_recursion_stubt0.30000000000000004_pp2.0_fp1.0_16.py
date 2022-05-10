import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    select.select(a, a, a)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0

        def close(self):
            a.pop()

    a.append(F())
    select.select(a, a, a)

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            return 0

        def close(self):
            a.pop()
            test_select_closed_mutated()

    a.append(F())
    select.select(a, a, a)

def test_select_closed_mutated_2():
    a = []

    class F:
        def fileno(self):
            return 0

        def close(self):
            a.pop()
            test_select_closed_mutated_2()

    a.append(F())
    select.select(a, a, a)

