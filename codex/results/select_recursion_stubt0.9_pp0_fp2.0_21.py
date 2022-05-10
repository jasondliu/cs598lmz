import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 5

    f = F()
    select.select([f], [f], [f], 0.0)
    assert a   # crashed when mutated by fileno()

def test_find_library_mutated():
    a = []

    class F:
        def fileno(slf):
            return 5

        def close(slf):
            test_find_library_mutated()
            a.append(1)

    f = F()
    select.select([f], [f], [f], 0.0)
    assert a   # crashed when mutated by close()

class FileObj:
    def __init__(self):
        from rpython.rlib import rwin32
        self.pos = 0
        self.handle = rwin32.get_osfhandle(self.fileno())

    def fileno(self):
        return 0

    def readinto(self, buf):
        lgt = len(buf)
        src = ("foobar" + chr(0))[self.pos:self.pos
