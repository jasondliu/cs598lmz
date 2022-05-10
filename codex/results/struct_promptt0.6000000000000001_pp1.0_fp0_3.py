import _struct
# Test _struct.Struct

def test_struct_compile():
    S = _struct.Struct("hhi")
    S = _struct.Struct("<hhi")
    S = _struct.Struct("<hhl")
    S = _struct.Struct("<hhi")
    S = _struct.Struct("b")
    S = _struct.Struct("bB")
    S = _struct.Struct("bBh")
    S = _struct.Struct("bBhH")
    S = _struct.Struct("bBhHI")
    S = _struct.Struct("bBhHIf")
    S = _struct.Struct("bBhHIfd")
    S = _struct.Struct("bBhHIfdp")
    S = _struct.Struct("bBhHIfdP")
    S = _struct.Struct("bBhHIfdPn")
    S = _struct.Struct("bBhHIfdPns")
    S = _struct.Struct("bBhHIfdPnsp")
    S = _struct.Struct("bBh
