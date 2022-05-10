import _struct

import pytest

from micropython import const
import uctypes

def test_struct_int():
    buf = bytearray(10)
    s = ustruct.pack("i", 0x12345678)
    assert s == b"xV\x12\x00"
    ustruct.pack_into("i", buf, 2, 0x12345678)
    assert buf == b"\x00\x00xV\x12\x00\x00\x00\x00\x00"
    assert ustruct.unpack("i", b"xV\x12\x00") == (0x12345678,)
    assert ustruct.unpack_from("i", b"\x00\x00xV\x12\x00\x00\x00\x00\x00", 2) == (0x12345678,)
