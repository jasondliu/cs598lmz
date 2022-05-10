import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    s = select.select([F()], [], [], 0)
    assert s[0] == []
    assert len(a) == 1
