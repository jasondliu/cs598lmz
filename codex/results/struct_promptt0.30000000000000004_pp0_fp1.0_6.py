import _struct
# Test _struct.Struct

import struct

def test_struct_error():
    try:
        _struct.Struct('abc')
    except struct.error:
        pass
    try:
        _struct.Struct('!')
    except struct.error:
        pass
    try:
        _struct.Struct('!i')
    except struct.error:
        pass
    try:
        _struct.Struct('!ii')
    except struct.error:
        pass
    try:
        _struct.Struct('!iii')
    except struct.error:
        pass

def test_struct_pack():
    s = _struct.Struct('!i')
    assert s.pack(1) == struct.pack('!i', 1)
    assert s.pack(1, 2) == struct.pack('!i', 1)
    assert s.pack(1, 2, 3) == struct.pack('!i', 1)
    assert s.pack(1, 2, 3, 4) == struct.pack('!i', 1)

def test_struct_unpack():
    s = _struct
