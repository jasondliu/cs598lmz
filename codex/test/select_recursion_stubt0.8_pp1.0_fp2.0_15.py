import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    x = select.select([], [F()], [], 0)
    # The above should raise IndexError, not segfault.
