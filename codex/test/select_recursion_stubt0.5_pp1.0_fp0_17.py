import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def close(self):
            a.append(1)

    f = F()
    select.select([f], [], [], 0)
    assert a == [1]
    f.close()

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            test_select_closed()
            return 0

        def close(self):
            a.append(1)

    f = F()
    f.close()
    select.select([f], [], [], 0)
    assert a == [1]
    f.close()

def test_select_closed_twice():
    a = []

    class F:
        def fileno(self):
            test_select_closed_twice()
            return 0

        def close(self):
            a.append(1)

    f = F()
    f.close()
    f.close()
    select.select([f], [], [], 0)
    assert a == [1]
    f.close()


