import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 100

    def select_f(*args):
        a.append(1)
        if len(a) == 2:
            del a[:]
            raise ValueError
        elif len(a) == 3:
            raise OSError
    select.select = select_f
    d = defer.Deferred()
    reactor.callWhenRunning(d.callback, None)
    del a[:]
    reactor.addReader(F())
    return d

def test_select_mutated_write():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_write()
            return 100

    def select_f(*args):
        a.append(1)
        if len(a) == 2:
            del a[:]
            raise ValueError
        elif len(a) == 3:
            raise OSError
    select.select = select_f
    d = defer.Deferred()
    reactor.callWhenRunning(d.callback, None)
    del a[:]
    reactor.add
