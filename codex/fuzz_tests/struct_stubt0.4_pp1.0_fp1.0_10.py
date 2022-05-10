from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4

def unpack(fmt, data):
    return s.unpack(data)

def pack(fmt, *data):
    return s.pack(*data)

def calcsize(fmt):
    return s.size

# end of 'if sys.version_info[0] < 3:'

# ______________________________________________________________________

def test_unpack():
    assert unpack('i', b'\x12\x34\x56\x78') == (0x12345678,)

def test_pack():
    assert pack('i', 0x12345678) == b'\x12\x34\x56\x78'

def test_calcsize():
    assert calcsize('i') == 4

# ______________________________________________________________________

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

# ______________________________________________________________________
# End of test_struct.py
