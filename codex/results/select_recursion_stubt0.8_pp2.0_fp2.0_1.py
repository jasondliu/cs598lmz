import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

        def fileno__(self):
            a.append(self)
            return -1

    f = F()
    select.select([f], [f], [f], 0)
    select.select([f], [f], [f], 0)
    assert a == [f, f]
    assert f.fileno() == -1

def test_select_attr_mutated():
    a = []

    class F:
        def __init__(self, value):
            self.value = value

        def fileno(self):
            test_select_attr_mutated()
            return -1

        def fileno__(self):
            a.append(self.value)
            return -1

    f = F(42)
    select.select([f], [f], [f], 0)
    select.select([f], [f], [f], 0)
    assert a == [42, 42]
    assert f.fileno() == -1

def test_select_mutated_key():
    a = []

    class
