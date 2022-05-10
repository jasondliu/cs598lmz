import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    b = []
    select.select([F()], [], [])
    print(a)
    del a[:]
    a.append(2)

test_select_mutated()
print("hello")
