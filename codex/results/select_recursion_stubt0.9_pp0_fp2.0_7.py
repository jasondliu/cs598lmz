import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    try:
        select.select([], [F()], [], 1.0)
    except NotImplementedError:
        pass
    else:
        raise AssertionError

if __name__ == '__main__':
    test_select_mutated()
