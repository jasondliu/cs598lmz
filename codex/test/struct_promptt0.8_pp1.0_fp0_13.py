import _struct
# Test _struct.Struct instances.
# from test import mapping_tests
import gc


def encode_decode(fmt, value):
    fmt = _struct.Struct(fmt)
    s = fmt.pack(*value)
    return fmt.unpack(s)


def test_bool(self):
    # bug 826894
    for fmt, value in [('b', (1,)), ('b', (-1,)), ('?'
        , (1,)), ('?', (-1,))]:
        self.assertEqual(encode_decode(fmt, value), value)


def test_pad(self):
    # bug 834007
    for fmt, value in [('xx', ()), ('xxxx', ()), ('2x2x', ()
        ), ('5p', ())]:
        self.assertEqual(encode_decode(fmt, value), value)


