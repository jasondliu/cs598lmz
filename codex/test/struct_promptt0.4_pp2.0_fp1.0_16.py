import _struct
# Test _struct.Struct.pack_into()

import array
import sys

def test_pack_into(format, args, expected):
    a = array.array("b", b"\0" * len(expected))
    s = _struct.Struct(format)
    s.pack_into(a, 0, *args)
    assert a.tobytes() == expected

def test_pack_into_native(format, args, expected):
    a = array.array("b", b"\0" * len(expected))
    s = _struct.Struct(format)
    s.pack_into(a, 0, *args)
    assert a.tobytes() == expected

def test_pack_into_little(format, args, expected):
    a = array.array("b", b"\0" * len(expected))
    s = _struct.Struct(format)
    s.pack_into(a, 0, *args)
    assert a.tobytes() == expected

def test_pack_into_big(format, args, expected):
    a = array.array
