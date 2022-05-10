import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    f = F()
    try:
        select.select([f], a, a, 0)
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"

if __name__ == "__main__":
    test_select_mutated()
