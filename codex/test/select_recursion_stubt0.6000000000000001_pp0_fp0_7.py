import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([F()], [], [])
    class X:
        pass
    select.select([X()], [], [])
    class X:
        def fileno(self):
            return len(a)

    select.select([X()], [], [])
    class X:
        def fileno(self):
            return len(a)

    select.select([X()], [], [])
    class X:
        def fileno(self):
            return len(a)

    select.select([X()], [], [])
    class X:
        def fileno(self):
            return len(a)

    select.select([X()], [], [])
    class X:
        def fileno(self):
            return len(a)

    select.select([X()], [], [])
    class X:
        def fileno(self):
            return len(a)

    select.select([X()], [], [])
    class X:
        def fileno(self):
            return
