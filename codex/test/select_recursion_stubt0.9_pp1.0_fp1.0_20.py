import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    # select modifies its first argument in place.
    a = select.select([F()], (), ()) or []
    del a[0]
