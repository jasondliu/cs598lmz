import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
    f = F()
    select.select([f], [], [], 0)
    test_select_mutated()
    assert a == [1]
