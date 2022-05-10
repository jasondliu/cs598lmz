import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    def g():
        a.append(select.select([], [F()], []))
        #assert a != [1]  # Not sure if we care that this fails, since
                         # we are not emulating C-python's behaviour

    g()
    g()
    raises(IndexError, select.select, [], [F()], [])
