import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

        def __getitem__(self, i):
            return a[i]

    f = F()
    select.select([f], [f], [f], 0.001)
    a.append(10)
    select.select([f], [f], [f], 0.001)
