import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    class L:
        def fileno(self):
            test_select_mutated()
            return 0

    try:
        select.select([f], [l], [])
    except ValueError:
        pass

if __name__=='__main__':
    test_select_mutated()
