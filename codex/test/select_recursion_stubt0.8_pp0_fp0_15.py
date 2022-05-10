import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def read(self):
            if not a:
                a.append(1)
                raise ValueError()
            else:
                a.append(2)
                raise RuntimeError()

    f = F()
    # select.select raises SysCallError, which is a subclass of
    # RuntimeError.  Obviously, we want ValueError to be raised and not
    # SysCallError.
    raises(ValueError, select.select, [f], [], [])
    assert a == [1, 2]

