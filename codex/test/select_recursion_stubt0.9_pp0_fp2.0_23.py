import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    def f():
        a.append(1)
        poll([f,])

    poll([F(),],) # raises an exception
    assert a == [1]

def test_select_timeout():
    for method in [select.select, select.poll]:
        selectable = method([], [], [], 1)
        assert isinstance(selectable, tuple)
        selectable = method([], [], [], 1.0)
        assert isinstance(selectable, tuple)
        try:
            selectable = method([], [], [], 1.5)
        except TypeError:
            pass
        selectable = method([], [], [], float(sys.maxsize))
        assert isinstance(selectable, tuple)
        selectable = method([], [], [], -1.5)
        assert isinstance(selectable, tuple)
        assert selectable == method([], [], [], None)
        selectable = method([], [], [], '1')
        assert isinstance(selectable, tuple)
