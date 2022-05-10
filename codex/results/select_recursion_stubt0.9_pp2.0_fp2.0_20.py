import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    s = select.select([], [F()], [])
    del s

if __name__ == '__main__':
    test_select_mutated()
