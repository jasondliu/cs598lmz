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

def dont_test_select_mutated_invalidated_exception_type():
    # Skip this for now.  This is about error handling in a rather
    # obscure corner of select.  Note that the original issue was
    # that after the ValueError from F, we got an OverflowError, even
    # though the next exception raised was a RuntimeError (!).  Only
    # after that exception did we have the correct behaviour.
    #
    # It's not clear what the right thing to do is.  As far as the
    # user is
