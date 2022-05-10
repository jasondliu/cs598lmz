import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated().append(1)
            return 1

    def f():
        select.select( [F()], [], [])

    # raise an error if the list is mutated
    f()
    raises(ValueError, f)
