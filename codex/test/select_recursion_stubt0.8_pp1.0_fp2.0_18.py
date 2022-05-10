import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    f = F()

    # This used to segfault because `select.select` was called again
    # on mutated lists.
    select.select([f], [f], [f], 0)

if __name__ == '__main__':
    test_select_mutated()
