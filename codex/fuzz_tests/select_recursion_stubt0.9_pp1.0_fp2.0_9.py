import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42
    a.append(F())

    rlist = a[:]
    while read_fds:
        select.select(read_fds, [], [])
    test_select_mutated()

def test_select_from_poll():
    # Issue #12501: Issue exceptions on underlying poll object if possible.
    class A:
        def fileno(self):
            raise OSError

        def poll(self, *_):
            raise OSError

    select.select([A()], [], [])
    with raisesRegex(OSError, "not supported"):
        select.select(
            [A(), -1], [], [], None, A())

class UnsupportedPoll(select.Poll):

    def register(self, fobj, *args):
        raise select.error('Not supported')

    def unregister(self, fobj):
        raise select.error('Not supported')

    def select(self, *args):
        raise select.error('Not supported')

def test_poll_from_select():
   
