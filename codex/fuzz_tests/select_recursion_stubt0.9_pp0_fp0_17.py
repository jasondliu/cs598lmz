import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # side-effect - 3 items added to a
            return 3
    s = [F(), F(), F(), F()]

    select.select(s, a, a)

    if s == [F(), F(), F(), F()]:
        raise Exception("Cannot detect neutered descriptors")
