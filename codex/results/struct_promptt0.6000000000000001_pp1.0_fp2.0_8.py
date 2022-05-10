import _struct
# Test _struct.Struct
def test_struct():
    class S(object):
        _pack_ = 1
        _fields_ = [('a', c_int16),
                    ('b', c_int32),
                    ('c', c_int8 * 4),
                    ('d', c_char_p),
                    ('e', c_wchar_p),
                    ('f', c_char * 4),
                    ('g', c_wchar * 4),
                    ('h', c_byte),
                    ('i', c_ubyte),
                    ('j', c_short),
                    ('k', c_ushort),
                    ('l', c_int),
                    ('m', c_uint),
                    ('n', c_long),
                    ('o', c_ulong),
                    ('p', c_longlong),
                    ('q', c_ulonglong),
                    ('r', c_size_t),
                    ('s', c_float),
                    ('t', c_double),
                    ('u', c_longdouble),
                    ('v', c_char_p),
                    ('w', c
