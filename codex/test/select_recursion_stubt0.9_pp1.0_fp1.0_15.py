import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    def r():
        return [F()]

    a[:] = [1, 2, 3]
    # The patch shouldn't be invoked directly by a call to
    # select.select, but instead be invoked by the side effect of the
    # fd returning the fileno() method
    select.select(r(), [], [], 1)

    a[:] = [1, 2, 3]
    try:
        select.select(r(), [], [], 1)
    except IndexError:
        pass
    else:
        assert False, "should have crashed"
