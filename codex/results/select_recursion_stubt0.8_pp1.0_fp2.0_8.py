import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def close(self):
            a.append(self)
            raise ValueError

    try:
        select.select([], [F(), F()], [])
    except ValueError:
        pass
    assert a
