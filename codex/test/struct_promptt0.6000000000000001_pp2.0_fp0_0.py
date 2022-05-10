import _struct
# Test _struct.Struct

import struct


def test_struct_new():
    a = _struct.Struct(">l")
    assert a.format == ">l"
    assert a.size == 4
    assert a.alignment == 4
    assert a.format_char == 'l'
    assert a.isnative is False
    assert a.byteorder == '>'
    assert a.fmt == '>l'

    a = _struct.Struct("<l")
    assert a.format == "<l"
    assert a.size == 4
    assert a.alignment == 4
    assert a.format_char == 'l'
    assert a.isnative is False
    assert a.byteorder == '<'
    assert a.fmt == '<l'

    a = _struct.Struct("l")
    assert a.format == "l"
    assert a.size == 4
    assert a.alignment == 4
    assert a.format_char == 'l'
    assert a.isnative is True
    assert a.byteorder == '@'
    assert a.f
