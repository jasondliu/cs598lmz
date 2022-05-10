import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    class E:
        def fileno(self):
            a.extend(range(10))
            return 2

    r, w, x = select.select([F(), E()], [], [])
    assert r == [2]
    assert a == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_error_conditions():
    import sys
    raises(ValueError, select.select, [], [], [], -1)
    raises(TypeError, select.select, [], [], [], 1j)
    raises(OSError, select.select, [3], [], [])
    if hasattr(sys, 'getcheckinterval'):
        n = sys.getcheckinterval()
        sys.setcheckinterval(1)
        try:
            raises(ValueError,
                    "import sys; "
                    "sys.setcheckinterval(0); "
                    "select.select([], [], [])")
        finally:
            sys.setcheckinterval(n)

