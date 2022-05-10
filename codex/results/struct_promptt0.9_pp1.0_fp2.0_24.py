import _struct
# Test _struct.Struct (issue #22079).
pack = _struct.Struct('>QQQQQQQQQQQQQQQ').pack
struct = _struct.Struct('>QQQQQQQQQQQQQQQ')
buf = bytearray(pack(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))
print('str(struct): {!r}'.format(str(struct)))
print('len(struct): {!r}'.format(len(struct)))
print('struct.pack: {}'.format(repr(struct.pack(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))))
print('struct.pack_into: {}'.format(struct.pack_into(buf,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)))
print('struct.unpack: {}'.format(repr(struct
