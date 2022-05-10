import _struct
# Test _struct.Struct
Format = _struct.Struct(b'h')
Returned = Format.pack(3)
Expected = b'\x03\x00'
if Returned != Expected:
    raise ValueError(
        "%a != %a" % (Returned, Expected)
    )
print(Returned)
