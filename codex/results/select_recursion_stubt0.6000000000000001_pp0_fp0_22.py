import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    select.select([], [F(), F()], [F()])
    a.append(1)
    assert a == [1]
