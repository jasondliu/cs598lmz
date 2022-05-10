import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    def f():
        select.select([F()], [], [])

    f()

class F(object):
    def fileno(self):
        return 12345
    def close(self):
        raise Exception

def test_select_close_fails():
    test_support.reap_children()
    r, w, x = select.select([F()], [], [])
    r[0].close()


class F1(object):
    def fileno(self):
        return 12345

class F2(F1):
    def fileno(self):
        return 67890

def test_select_bad_args():
    test_support.reap_children()
    # Test various bad arguments to select().
    raises(TypeError, select.select, "1", 2, 3)
    raises(TypeError, select.select, [1, 2, 3], "1", 3)
    raises(TypeError, select.select, [1, 2, 3], [2, 3, 4], "1")
