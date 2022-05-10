import _struct
# Test _struct.Struct


class SignedTest:
    kind = "signed"

    def test_bool(self):
        for fmt, expected in self.format_examples:
            S = _struct.Struct(fmt)
            s = S.pack(True)
            v, = S.unpack(s)
            self.assertEqual(v, expected)

    def test_bool_nonzero(self):
        for fmt, expected in self.format_examples:
            S = _struct.Struct(fmt)
            s = S.pack(42)
            v, = S.unpack(s)
            self.assertEqual(v, expected)

    def test_bool_zero(self):
        for fmt, expected in self.format_examples:
            S = _struct.Struct(fmt)
            s = S.pack(0)
            v, = S.unpack(s)
            self.assertEqual(v, expected)

    def test_bool_error(self):
        for fmt, expected in self.format_examples:
            S = _struct
