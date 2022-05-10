import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    class G:
        def fileno(self):
            a.append(1)
            return 2

    select.select([F(), G()], [], [])
    assert a == [1]

def test_select_removed():
    a = []

    class F:
        def fileno(self):
            test_select_removed()
            return 1

    class G:
        def fileno(self):
            a.append(1)
            return 2

    select.select([F(), G()], [], [])
    assert a == [1]
