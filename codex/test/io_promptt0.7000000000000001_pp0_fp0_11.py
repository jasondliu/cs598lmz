import io
# Test io.RawIOBase.readinto()

import io
import array
import unittest

class TestReadinto(unittest.TestCase):
    def test_readinto(self):
        # This is an almost exact copy of StringIO.readinto()
        def readinto(self, b):
            l = len(b) # we're supposed to update the BytesIO object
            s = self.read(l)
            n = len(s)
            try:
                b[:n] = s
            except TypeError as err:
                import array
                if not isinstance(b, array.array):
                    raise err
                b[:n] = array.array(b'b', s)
            return n

        f = io.BytesIO()
        f.write(b'xyz')
        f.seek(0)
        b = bytearray(3)
        n = readinto(f, b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b'xyz')

        # SF bug 534662
        f
