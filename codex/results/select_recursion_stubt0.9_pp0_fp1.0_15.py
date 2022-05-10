import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(0)
            return False

    select.select([F()], [F()], [F()], 1)
    assert a == []
    test_select_mutated()
    print 'select: ok'

test_select_mutated()
