import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

        def __call__(self):
            return a

    def g():
        return a

    def gen():
        yield a

    for s in [a, gen(), g(), F()()]:
        # This tests for an infinite loop when the underlying file descriptor
        # object is replaced.
        try:
            select.select([s], [s], [s])
        except OSError as e:
            # On Mac OS X and BSD, select() doesn't respond well to the removal
            # of all entries under the file descriptor object.
            if not (sys.platform == "darwin" or sys.platform.startswith("freebsd")):
                raise e
        except RuntimeError as e:
            if "lists mutated during iteration" not in str(e):
                raise e


class GeneralTests(unittest.TestCase):
    def test_list_mutated(self):
        # XXX: This test shouldn't exist because list mutations shouldn't
        # cause undefined behavior in the caller.
        test_select_mutated()
                         
