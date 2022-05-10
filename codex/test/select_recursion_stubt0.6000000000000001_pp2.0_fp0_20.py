import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    x = select.select([F()], a, a, 0)
    assert x == ([], [], [])
