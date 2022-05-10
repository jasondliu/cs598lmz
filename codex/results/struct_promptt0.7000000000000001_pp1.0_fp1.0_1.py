import _struct
# Test _struct.Struct from struct module

import struct as st, _struct as s

def test_format(format, value, expected):
    try:
        sval = st.Struct(format).pack(*value)
    except Exception as e:
        sval = e
    try:
        uval = s.Struct(format).pack(*value)
    except Exception as e:
        uval = e
    if sval != uval:
        raise Exception('struct and _struct disagree on %s %s: %r vs %r' %
                (format, value, sval, uval))
    if repr(sval) != repr(expected):
        raise Exception('expected %r, got %r' % (expected, sval))

def test_unpack(format, data, expected):
    try:
        sval = st.Struct(format).unpack(data)
    except Exception as e:
        sval = e
    try:
        uval = s.Struct(format).unpack(data)
    except Exception as e:
        uval = e
    if sval != u
