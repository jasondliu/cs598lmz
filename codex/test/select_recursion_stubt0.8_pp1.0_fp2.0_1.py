import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

        def foo(self):
            a.append(self)

    select.select([F()], [], [])

