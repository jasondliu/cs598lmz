import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    # Calling select.select on a mutating list should not segfault.
    select.select([F()], a, a, 0)
