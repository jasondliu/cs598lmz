import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # surprise!
            return a.pop()

    try:
        select.select([F()], [F()], [F()], 0)
    except IndexError:
        pass
    except ValueError:
        pass
    except select.error:
        pass
    else:
        raise AssertionError("select should have raised some exception")

def test_select_closedfd():
    try:
        select.select([], [], [-1])
    except select.error as e:
        msg = str(e)
        if msg and msg[0] == 'Bad' and msg[-1] == 'file descriptor':
            return
    except Exception as e:
        msg = str(e)
        if msg and msg[0] == 'Bad' and msg[-1] == 'file descriptor':
            return
    raise AssertionError("select raised %s and not 'Bad file descriptor'" % e)

def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated() # surprise!

