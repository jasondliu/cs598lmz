import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5
        def close(self):
            a.append(1)

    select.select([f], [], [])
    del f
    test_select_mutated()
    import gc
    gc.collect()
    assert a == [1]

class MyFile:
    def __init__(self, name):
        self.name = name
        self.closed = 0
        self.softspace = 0

    def fileno(self):
        return self.name

    def close(self):
        self.closed = 1

    def flush(self):
        pass

    def write(self, s):
        pass

    def writelines(self, l):
        pass

    def read(self, n=-1):
        return ''

    def readline(self, length=None):
        return ''

    def readlines(self, sizehint=0):
        return []

    def seek(self, offset, whence=0):
        pass

    def tell(self):
        return 0

