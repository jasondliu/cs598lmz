import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    sel = select.select([F()], [], [], 0)[0]
    sel[0].fileno()
    print("done")


# select_test.test_select_mutated()

def test_select_keyboardinterrupt1():
    # The problem here is that the select() call is interrupted with a
    # KeyboardInterrupt error, and we didn't check properly if the file
    # descriptor is actually ready.

    def f(*args):
        raise KeyboardInterrupt

    class F(object):
        def fileno(self):
            return 0
    try:
        select.select([F()], [], [], 0, f)
    except KeyboardInterrupt:
        pass
    else:
        raise AssertionError("Expected a KeyboardInterrupt")

#@skip("multi_process")
def test_select_keyboardinterrupt2():
    # Same as above, but the exception is raised in a different thread.
    # This case is more difficult to handle.

    def f():
        import time
        time
