import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    fs = F()
    select.select([fs], [], [], 0)
    del a[:]

class F(object):
    def fileno(self):
        return 1

# check that the list of file descriptors is copied
def test_select_mutated2():
    fs = F()
    select.select([fs], [fs], [fs], 0)
    del fs.__dict__

def test_select_mutated3():
    fs = F()
    select.select([fs], [fs], [fs], 0)
    del F.fileno

def test_select_mutated4():
    fs = F()
    select.select([fs], [fs], [fs], 0)
    F.fileno = lambda self: 2

def test_select_mutated5():
    fs = F()
    select.select([fs], [fs], [fs], 0)
    F.fileno = lambda self: 'invalid'

def test_select_mutated6():
    fs = F()
   
