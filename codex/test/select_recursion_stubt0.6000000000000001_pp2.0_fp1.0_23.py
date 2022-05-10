import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
        def do_select(self, r, w, x):
            a.append(self)
            return r, w, x

    f = F()
    select.select([f], [f], [f], 0)
    assert a[0] is f

if __name__ == "__main__":
    test_select_mutated()
