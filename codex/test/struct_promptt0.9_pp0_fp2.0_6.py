import _struct
# Test _struct.Struct on bytes 
class StructTest(unittest.TestCase):
    types = 'bBhHiIlLqQfdspP'
    if _struct.HAVE_LARGE_NUMBERS:
        types += 'QQ'

    def _test_bin_roundtrip(self, code):
        s = _struct.Struct(code)
        for formatchar, typefunc in zip(self.types, self.typefuncs):
            format = code % formatchar
            st = s.pack(typefunc(0), typefunc(1), typefunc(42), typefunc(-1), typefunc(-42), typefunc(sys.maxsize), typefunc(-sys.maxsize + 1))
            self.assertEqual(s.size, len(st))
            if sys.byteorder == 'big':
                self.assertEqual(st, _struct.calcsize(format))
            else:
                self.assertEqual(st, _struct.calcsize(format))
            unpacked = s.unpack(st)
