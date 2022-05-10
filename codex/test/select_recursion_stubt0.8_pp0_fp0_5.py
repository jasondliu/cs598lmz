import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    select.select([f], [], [], 0)
    a.append(1)

    if not a:
        print("hello")
    select.select([f], [], [], 0)
    a.append(1)

    if a:
        print("hello")
    select.select([f], [], [], 0)


test_select_mutated()
