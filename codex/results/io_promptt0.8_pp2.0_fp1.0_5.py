import io
# Test io.RawIOBase
import io
from io import UnsupportedOperation

from test import support


class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        b = io.RawIOBase()
        self.assertEqual(hasattr(b, 'mode'), False)
        self.assertEqual(hasattr(b, 'name'), False)


class RawIOBaseTest(unittest.TestCase):

    def test_args(self):
        # Test argument names
        self.assertEqual(io.RawIOBase.read.__code__.co_varnames,
                         ('self', 'n'))
        self.assertEqual(io.RawIOBase.readline.__code__.co_varnames,
                         ('self', 'limit'))
        self.assertEqual(io.RawIOBase.write.__code__.co_varnames,
                         ('self', 'b'))
        self.assertEqual(io.RawIOBase.fileno.__code__.co_varnames,
                         ('self',
