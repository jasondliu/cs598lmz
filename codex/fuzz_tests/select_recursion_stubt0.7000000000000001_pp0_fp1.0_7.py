import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    sel = select.select([F()], a, a)
    assert sel == ([], [], [])
    assert a == [], 'select mutated its argument'
