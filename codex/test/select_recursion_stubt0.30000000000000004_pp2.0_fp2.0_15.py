import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [])
    select.select([], [F()], [])
    select.select([], [], [F()])

def test_select_interrupted():
    a = []

    class F:
        def fileno(self):
            test_select_interrupted()
            return 0

    try:
        select.select([F()], [], [])
    except select.error as e:
        assert e.args[0] == errno.EINTR
    else:
        assert False, "select() should raise EINTR"

    try:
        select.select([], [F()], [])
    except select.error as e:
        assert e.args[0] == errno.EINTR
    else:
        assert False, "select() should raise EINTR"

    try:
        select.select([], [], [F()])
    except select.error as e:
        assert e.args[0] == errno.EINTR
