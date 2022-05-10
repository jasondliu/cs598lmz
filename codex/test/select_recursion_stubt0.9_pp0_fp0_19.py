import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    f = F()
    select.select([f], [], [], 0)
    assert not a
    del f
    test_select_mutated()
    assert a == []

class TestException:

    class BadFD:
        def __init__(self, fileno):
            self.fileno = fileno
        def fileno(self):
            return self.fileno

        def __repr__(self):
            return "<BadFD, fd %i>" % self.fileno

    class GoodFD:
        def __init__(self, fileno):
            self.fileno = fileno
        def fileno(self):
            return self.fileno

    def setup_class(self):
        global os, select, socket

        os = __import__(os.name)

        self.old_select = select.select

        if sys.platform == 'win32':
            self.valid_fd_start = 1
        else:
            self.valid_fd_start = 0

