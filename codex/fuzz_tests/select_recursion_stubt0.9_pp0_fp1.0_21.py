import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # change fds after select.select() did, so it poll them
            a.append(0)
            return 1
        def read(self):
            raise StopIteration

    assert select.select([F()],[],[],1) == ([],[],[])
    raises(ValueError, select.select, [a], [a], [a], 1)
    raises(ValueError, select.select, [a], [a], [a], -1)
    assert select.select([a], [a], [a], 0) == ([], [], [])
    assert select.select([a], [a], [a], 0.5) == ([], [], [])
    raises(ValueError, select.select, [a], [a], [a], -0.5)

class MyFd:
    def __init__(self):
        self.read_num = 0
    def fileno(self):
        return 1
    def read(self):
        self.read_num += 1
        return ''

def test_select_timeout():
    fd = MyFd()

