import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0 # Try to make this happen.  (In practice, this is probably going to cause a crash.)

    a.append(F())
    select.select([], [], a)
