import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(4)
    select.select([f], [], [], 0)
    a.append(5)
    select.select([f], [], [], 0)
    a.append(6)
    select.select([f], [], [], 0)

def main():
    test_select_mutated()

main()
