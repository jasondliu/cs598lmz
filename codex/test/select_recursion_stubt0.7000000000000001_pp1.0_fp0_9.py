import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    select.select([], [F()], a, 0)

    assert len(a) == 0


def test_select_fileno_attr():
    class F:
        def __getattr__(self, name):
            if name == 'fileno':
                return lambda: -1
            return AttributeError
    a = select.select([F()], [], [], 0)
    assert len(a[0]) == 0
    assert len(a[1]) == 0
    assert len(a[2]) == 0

def test_select_error_attr():
    class F:
        def __getattr__(self, name):
            if name == 'fileno':
                return lambda: -1
            return AttributeError
    a = select.select([F()], [], [], 0)
    assert len(a[0]) == 0
    assert len(a[1]) == 0
    assert len(a[2]) == 0

def test_select_non_ints():
    class C:
        pass
