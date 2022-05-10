import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    def xreadlines():
        a.append(F())
        yield a[-1]

    x = xreadlines()
    # This should not crash
    select.select([x],[],[])

class MyIO(io.BytesIO):
    def read(self, n=-1):
        return b"x" * 100

class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b"x" * 100

class TestSelect(unittest.TestCase):
    def test_error_conditions(self):
        # Select must raise ValueError if passed empty lists or lists with
        # non-integer objects
        self.assertRaises(ValueError, select.select, [], [], [])
        self.assertRaises(ValueError, select.select, [[]], [[]], [[]])
        self.assertRaises(TypeError, select.select, [1], [2], [3])

        # But if not passed enough arguments, select() ignores the TypeErrors
        def
