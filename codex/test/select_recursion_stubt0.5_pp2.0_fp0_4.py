import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 5

    f = F()
    select.select([f], [], [], 1)
    assert a
