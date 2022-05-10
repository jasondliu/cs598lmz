import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    a.append(f)

    select.select([f], [], [], 0.1)

    assert len(a) == 0
