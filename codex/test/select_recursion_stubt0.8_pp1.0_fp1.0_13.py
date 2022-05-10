import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

        def read(self):
            a.append(1)

    f = F()
    select.select([f], [f], [f])

    # it's ok to continue, but we should have seen the exception
    assert a == [1]
