import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return f.fileno()

    f = F()
    a.append(f)
    select.select([f], [], [])

if sys.platform[:3] != 'win':
    # The regression check tests that poll.poll modifies poll object
    # even if select was interrupted earlier by a signal.

    import pickle

