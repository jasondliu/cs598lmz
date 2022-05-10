import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0)

def test_select_keyboardinterrupt_eintr():
    # Issue 4749: select.select() should raise KeyboardInterrupt on EINTR
    class F:
        def fileno(self):
            raise IOError(errno.EINTR, "EINTR")

    # Can't use a with statement here because it's not supported in 2.4
    # and the select module is used in the implementation of
    # socket.create_connection()
    f = open(support.TESTFN, "wb")
    try:
        try:
            select.select([f, F()], [], [])
        except IOError, e:
            assert e.errno == errno.EINTR
        else:
            assert False, "IOError with errno.EINTR not raised"
    finally:
        f.close()
        support.unlink(support.TESTFN)

if __name__ == "__main__":
    test_select_mutated()
   
