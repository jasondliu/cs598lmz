import _struct
# Test _struct.Struct.from_format
from _struct import Struct

from test import support

from test.support import bigmemtest


def test_from_format():
    Struct.from_format
    s = Struct.from_format("")
    assert s.size == 0
    assert s.format == ""
    s = Struct.from_format("i")
    assert s.size == 4
    assert s.format == "i"
    s = Struct.from_format("ii")
    assert s.size == 8
    assert s.format == "ii"
    s = Struct.from_format("=i")
    assert s.size == 4
    assert s.format == "=i"
    s = Struct.from_format("=ii")
    assert s.size == 8
    assert s.format == "=ii"
    s = Struct.from_format("@i")
    assert s.size == 4
    assert s.format == "@i"
    s = Struct.from_format("@ii")
    assert s.size == 8
    assert s.format == "@ii"

