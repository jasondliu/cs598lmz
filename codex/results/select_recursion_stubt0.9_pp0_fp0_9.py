import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    for fn in [-10, -11, -3]:
        a.append(fn)
        f = F()
        try:
            select.select([f], [f], [f])
        except (ValueError, select.error) as e:
            # XXX: Windows reports different exception classes.
            assert e.args[0] == errno.EBADF
        else:
            assert False, "DID NOT TRAP"

def test_select_mutated_2():
    # just like test_select_mutated(), but ReadWriteDescriptor is builtin.
    import os
    a = []

    class F:
        def fileno(self):
            return a.pop()

    for fn in [-10, -11, -3]:
        a.append(fn)
        f = F()
        try:
            os.select([f], [f], [f])
        except OSError as e:
            # XXX: Windows reports different exception classes.
            assert e.args[0] == errno.EBAD
