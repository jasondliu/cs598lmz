import _struct
# Test _struct.Struct
x = _struct.Struct('i')
x.size
x.pack(42)
x.unpack(_struct.pack('i', 42))
x.unpack(_struct.pack('i', -42))
x.unpack(_struct.pack('i', 0))
x.pack_into(b'\0'*4, 0, 42)
x.unpack_from(_struct.pack('i', 42), 0)
x.unpack_from(_struct.pack('i', -42), 0)
x.unpack_from(_struct.pack('i', 0), 0)
x = _struct.Struct('>ii')
x.size
x.pack(4200, 4300)
x.unpack(_struct.pack('>ii', 4200, 4300))
x.unpack(_struct.pack('>ii', -4200, -4300))
x.unpack(_struct.pack('>ii', 0, 0))
x.pack_into(b'\0'*8, 0, 4200, 4300)
x.unpack_from(_struct.pack('
