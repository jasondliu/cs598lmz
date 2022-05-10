import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append('fileno')
            return -1

    f = F()
    try:
        select.select([f], [f], [f], 0.0)
    except AttributeError:
        pass
    del f
    #assert not a, a
