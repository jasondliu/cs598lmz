import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1
        def close(self):
            a.append(1)

    select.select([], [], [F()])
    assert a == [1]
