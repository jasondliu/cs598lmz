import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 10
    a.append(F())

    try:
        select.select([], a, a, 0)
    except ValueError:
        pass

    a.pop()
    try:
        select.select([], a, a, 0)
    except ValueError:
        pass

def main():
    test_select_mutated()
    test_select_mutated()

main()
