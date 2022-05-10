import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    select.select([F()], [F()], [F()], 0)
    assert_raises(RuntimeError, select.select, [F()], [F()], [F()], 0)

def test_all_1():
    info = select.__doc__ + select.select.__doc__
    assert "*** OSError" in info
    assert "***  exception" in info
