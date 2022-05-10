import _struct
# Test _struct.Struct class

i16_le_struct = _struct.Struct('<h')
i16_be_struct = _struct.Struct('>h')

for i in (-1, 0, 1, 2, 3, 4, 5, 20, 1000, 0x7FF0, 0x7FFF, -20000):
    encoded = i16_le_struct.pack(i)[0]
    try:
        b1 = (i & 0xFF00) >> 8
        b2 = i & 0xFF
        expected = b1 ^ b2
    except OverflowError:
        expected = 0xFF
    #print(encoded, expected)
    assert encoded == expected
 
for i in i16_be_struct.pack(-1):
    assert i == 0xFF

# Test _struct.unpack class

i16_le2_struct = _struct.Struct('<HH')

encoded = i16_le2_struct.pack(-1, 1)[0]
assert encoded == 0xFF
