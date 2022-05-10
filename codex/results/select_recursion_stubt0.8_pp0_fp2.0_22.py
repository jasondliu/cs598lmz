import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.insert(0, True)

    f = F()
    select.select([f], [f], [f])
    assert a

if __name__ == "__main__":
    test_select_mutated()
