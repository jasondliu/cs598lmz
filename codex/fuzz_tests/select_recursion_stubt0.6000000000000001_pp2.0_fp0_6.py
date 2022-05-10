import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())

    try:
        a.append(F())
        select.select(a, [], [], 0)
    except ValueError:
        pass
    else:
        assert 0, "failed to catch a mutated object list"
