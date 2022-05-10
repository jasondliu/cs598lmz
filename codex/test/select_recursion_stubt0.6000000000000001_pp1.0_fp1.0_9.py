import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    s = select.select([F()], [], [], 0)
    assert len(s) == 3
    assert len(s[0]) == 0
    assert len(s[1]) == 0
    assert len(s[2]) == 0
