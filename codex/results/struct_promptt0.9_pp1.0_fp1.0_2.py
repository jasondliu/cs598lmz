import _struct
# Test _struct.Struct

s = _struct.Struct('i7sf')

class IndexTest(unittest.TestCase):
    def check(self, result, ind):
        self.assertEqual(result, ind)

    def test_index(self):
        for arg in [0, 1, 2, -1, -2, -3, -4]:
            self.check(s.index('i', arg), 1)
            self.check(s.index('7', arg), 2)
            self.check(s.index('s', arg), 3)
            self.check(s.index('f', arg), 4)
            with self.assertRaises(ValueError):
                s.index('c', arg)
            with self.assertRaises(ValueError):
                s.index('c')
            with self.assertRaises(IndexError):
                s.index('i', arg, 1)

    def test_index_error(self):
        with self.assertRaises(IndexError):
            s.index('i', -5)
        with self.assertRaises(Index
