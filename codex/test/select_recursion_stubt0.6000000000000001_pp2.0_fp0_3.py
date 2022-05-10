import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 0

    select.select([F()], [], [], 0.1)
    assert a == [1]
