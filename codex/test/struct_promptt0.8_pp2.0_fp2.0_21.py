import _struct
# Test _struct.Struct methods that are not used by the module
from test.test_structmembers import StructTestCase
class TestStruct(StructTestCase):
    def test_unpack(self):
        class X:
            def __init__(self, iterable):
                self.iterable = iterable
            def read(self, n):
                iterable = self.iterable
                L = []
                for i in range(n):
                    try:
                        L.append(next(iterable))
                    except StopIteration:
                        break
                return bytes(L)
        for format, size, value, expected in self.size_values:
            s = _struct.Struct(format)
            self.assertEqual(s.unpack(X(iter(value))), expected)
    def test_unpack_from(self):
        class X:
            def __init__(self, bytes):
                self.bytes = bytes
                self.offset = 0
            def read(self, n):
                b = self.bytes
                i = self.offset
                if i >= len(b):
                    raise
