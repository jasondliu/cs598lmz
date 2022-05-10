import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    b = F()
    select.select([b], [], [])
    assert a == [1]

def test_select_error():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            a.append(1)
            raise ValueError

    b = F()
    py.test.raises(ValueError, "select.select([b], [], [])")
    assert a == [1, 1]

def test_select_cannot_mutate():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            a.append(1)
            raise ValueError

    b = F()
    py.test.raises(ValueError, "select.select([b], [], [])")
    assert a == [1, 1]

def test_select_error_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            raise Value
