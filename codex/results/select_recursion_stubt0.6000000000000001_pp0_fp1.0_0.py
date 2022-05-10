import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    select.select([], [], a)
    a.append(F())
    select.select([], [], a)

def test_select_keyboardinterrupt():
    a = []

    class F:
        def fileno(self):
            raise KeyboardInterrupt

    a.append(F())
    select.select([], [], a)

def test_select_keyboardinterrupt2():
    a = []

    class F:
        def fileno(self):
            raise KeyboardInterrupt

    a.append(F())
    try:
        select.select(a, [], [])
    except select.error as e:
        assert e.args == (errno.EINTR, "Interrupted system call")
    else:
        assert False, "select.error not raised"

def test_select_keyboardinterrupt3():
    a = []

    class F:
        def fileno(self):
            raise KeyboardInterrupt

    a.append(F())
    select.select([], a, [
