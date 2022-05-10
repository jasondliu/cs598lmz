import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    s = select.select([], [], [F()])
    exc_type, exc, tb = sys.exc_info()
    raise exc_type(exc).with_traceback(tb)
