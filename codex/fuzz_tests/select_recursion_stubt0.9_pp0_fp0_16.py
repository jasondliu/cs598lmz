import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 3
    a.append(F())

    class G:
        def fileno(self):
            return 5
    a.append(G())

    # checks if a is mutated
    try:
        select.select(a, [], [], 0)
    except IndexError:
        pass
    else:
        py.test.fail("select.select() mutated objects")

def test_select_returning_none():
    import select

    class ReturnNone:

        def fileno(self):
            return None

    assert select.select([], [ReturnNone()], [], 0.1) == ([], [], [])


class AppTestSelect:

    def setup_class(cls):
        space = gettestobjspace(usemodules=('select',))
        cls.space = space

    def setup_method(self, meth):
        # This function make sure that we don't see any floats in time
        # comparison (time.time() returns a float object)
        import time
        time.time = lambda: 50000.0

        # Create a server
