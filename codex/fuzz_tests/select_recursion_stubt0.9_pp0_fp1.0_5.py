import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5

    f, g, h = F(), F(), F()
    select.select([f], [g], [h])
    a.append(42)
    return a

a = test_select_mutated()
print(a)
