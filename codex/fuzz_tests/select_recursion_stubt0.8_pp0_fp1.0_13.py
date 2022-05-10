import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()

    try:
        select.select([f], [f], [f])
    except ValueError:
        pass
    else:
        print("lost ValueError from select on mutated object")

def test_select_err():
    # In issue #5716, a bug in select.error handling caused an AttributeError.
    try:
        select.select([], [], [], -1.0)
    except select.error as e:
        assert e.args == (-1, 'EBADF')
    except:
        print("lost select.error exception")

def test_select_fds():
    # Issue #5716
    try:
        select.select([""], [], [], 0.0)
    except TypeError as e:
        assert "an integer" in str(e)
    else:
        print("lost TypeError trying to select on a string")

def test_select_timeout():
    try:
        select.select([], [], [], -1.0)
    except ValueError
