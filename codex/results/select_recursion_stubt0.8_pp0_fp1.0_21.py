import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    obj = F()
    a.append(obj)
    try:
        select.select([obj], [], [])
    except ValueError:
        pass

def test_select_keyboard_interrupt():
    # select([fobj], [], []) raises KeyboardInterrupt from
    # interrupt_select_call()
    class F:
        def fileno(self):
            return -1
    try:
        select.select([F()], [], [], timeout=0.)
    except KeyboardInterrupt:
        pass
    else:
        assert False, "KeyboardInterrupt not raised"

def test_select_error_conditions():
    # issue3697
    l = []

    class F(object):

        def fileno(self):
            l.append(self)
            try:
                select.select([self], [self], [self], timeout=0.5)
            except select.error as e:
                assert e.args[0] == errno.EBADF
            else:
                assert False,
