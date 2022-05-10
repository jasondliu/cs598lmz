import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [F()], [F()], 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            test_select_closed()
            return a.pop()

        def close(self):
            a.append(None)

    select.select([F()], [F()], [F()], 0)

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_closed_mutated()
            return a.pop()

        def close(self):
            a.append(None)

    select.select([F()], [F()], [F()], 0)

def test_select_closed_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_closed_mutated_2()
            return a.pop()

        def close(self):
            a.append(None)

