import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
    fobj = F()
    a.append(fobj)
    for i in range(10):
        try:
            select.select([fobj], [], [], 0)
        except TypeError:
            pass
        else:
            assert False, "expected TypeError"

class MyException(Exception):
    pass

def test_select_keyboardinterrupt():
    class R:
        def fileno(self):
            raise MyException()
    class W:
        def fileno(self):
            raise KeyboardInterrupt()
    r = R()
    w = W()
    try:
        select.select([r], [w], [], 0.1)
    except MyException:
        pass
    else:
        assert False, "MyException should have been raised"

def test_select_keyboardinterrupt2():
    class R:
        def fileno(self):
            raise KeyboardInterrupt()
    class W:
        def fileno(self):
            raise MyException()
    r = R()
    w = W
