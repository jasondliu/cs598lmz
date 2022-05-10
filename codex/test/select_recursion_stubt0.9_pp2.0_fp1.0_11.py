import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    try:
        select.select([F()], a, a, a)
    except OSError as e:
        pass
    else:
        print("avoid this yo")
        print("https://bugs.python.org/issue18394")
        assert False

test_select_mutated()
