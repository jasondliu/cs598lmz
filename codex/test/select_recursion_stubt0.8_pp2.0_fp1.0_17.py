import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
    select.select([F()], [], [])
    select.select([], [F()], [])
    select.select([], [], [F()])

def test_select_mutated_broken():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_broken()
            a.append(1)
            return True

    try:
        test_select_mutated_broken()
    except:
        pass
    try:
        select.select([F()], [], [])
    except ValueError:
        pass
    try:
        select.select([], [F()], [])
    except ValueError:
        pass
    try:
        select.select([], [], [F()])
    except ValueError:
        pass

