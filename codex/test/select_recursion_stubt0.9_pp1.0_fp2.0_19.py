import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)
            raise AssertionError()

    def doit():
        select.select([F()], [], [])
    doit()
