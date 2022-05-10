import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop(0)

    # need to be able to call fileno() several times
    with pytest.raises(IndexError):
        select.select([F()], [F()], [F()], 0)

    # but the underlying file gets closed
    pytest.raises(OSError, F().fileno)


# Issue 1711946
class MyFileObject(object):
    def __init__(self, name, mode='rb'):
        self.name = name
        self.mode = mode
        self.closed = False
        if self.mode not in ('rb', 'wb'):
            raise ValueError("invalid mode: %r" % self.mode)

    def __repr__(self):
        s = str(self.name)
        if self.closed:
            s += " (closed)"
        s += " in %s mode" % self.mode
        return "<%s at %#x>" % (s, id(self))

    def close(self):
        self.closed = True

    def fileno(self):

