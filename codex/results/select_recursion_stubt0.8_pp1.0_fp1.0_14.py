import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [], 0)
    select.select([], [F()], [], 0)
    select.select([], [], [F()], 0)

    test_select_mutated.a = []

    try:
        select.select([], [], [], -1)
    except ValueError:
        pass
