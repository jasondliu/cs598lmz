import _struct
# Test _struct.Struct, _struct.pack, _struct.unpack.

# Format strings
fmt1 = 'hhl5s'
fmt2 = 'hhl'
fmt3 = '5s'
fmt4 = 'hhhhi'
fmt5 = 'i'
fmt6 = 'hhlih'

# Values
values1 = (1, 2, 3, b'abc')
values2 = values1[:3]
values3 = values1[3:]
values4 = (1, 2, 3, 4, 5)
values5 = (1,)
values6 = (1, 2, 3, 4, 5, 6)

# Test pack
packed1 = _struct.pack(fmt1, *values1)
packed2 = _struct.pack(fmt2, *values2)
packed3 = _struct.pack(fmt3, *values3)
packed4 = _struct.pack(fmt4, *values4)
packed5 = _struct.pack(fmt5, *values5)
