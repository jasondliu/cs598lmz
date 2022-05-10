import _struct
# Test _struct.Struct and _struct.pack/unpack/calcsize

import struct as st


class S(st.Struct):
    _fmt = 'HH'
    _fields = None


class S2(st.Struct):
    _fmt = 'B3s'
    _fields = ['foo', 'bar']

class S3(st.Struct):
    _fmt = '3B3s'
    _fields = ['foo', 'bar', 'baz', 'etc']

class S4(st.Struct):
    _fmt = '3B3s'
    _fields = ('foo', 'bar', 'baz', 'etc')

class S5(st.Struct):
    _fmt = 'i'


class S6(st.Struct):
    _fmt = 'P'
    _itemize = st._itemize_int_base


test_values = [(1234, 5678),
               (255, b'abc')]


def test_unpack():
    for test_value in test_values:
        s = S(*test_
