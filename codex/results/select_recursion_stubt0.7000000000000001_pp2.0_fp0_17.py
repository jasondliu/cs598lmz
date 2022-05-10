import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

    select.select([], [F()], [], 0)

    a.append(1)
    a.append(2)
    a.append(3)

def main():
    for i in xrange(100):
        test_select_mutated()

main()
