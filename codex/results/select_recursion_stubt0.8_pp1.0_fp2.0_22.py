import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 3
        def close(self):
            a.append(1)
    f = F()
    select.select([f], [], [], 0.0)
    assert a == [1]
