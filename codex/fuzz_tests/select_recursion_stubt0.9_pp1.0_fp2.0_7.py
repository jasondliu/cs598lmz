import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 4
    a.append(F())
    a.append(F())
    a.append(F())
    a.append(F())

    print(select.select([], a, a, 42))

class F:
    def __init__(self):
        self.i = 1

    def fileno(self):
        self.i += 1
        if self.i > 3:
            self.i = 0
        if self.i == 1:
            raise OSError('file number 1 not allowed')
        return self.i

def test_file_closed():
    print(select.select([F()], [], []))

def test_file_not_closed():
    try:
        test_file_closed()
    except OSError:
        print('OK')

def test_simplified_select():
    from pypy.rpython.lltypesystem import rffi
    import pypy.translator.c.test.test_genc
    from pypy.translator.c.genc import C
