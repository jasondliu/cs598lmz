import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    select.select([a], [], [F()], 1)
    a.append(1)

def main():
    test_select_mutated()

main()
