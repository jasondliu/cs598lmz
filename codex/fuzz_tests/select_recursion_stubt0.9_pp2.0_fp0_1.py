import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return -1

    try:
        select.select([F()], [F()], [], 0)
    except ValueError:
        pass
