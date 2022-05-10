import _struct
# Test _struct.Struct constructor
struct = _struct.Struct('i')
len(struct.pack(1)) == 4
struct.pack.__self__ is struct
struct.unpack.__self__ is struct
struct.size == 4
struct.unpack(struct.pack(1)) == (1,)
struct.format == 'i'
struct.pack_into.__self__ is struct
struct.unpack_from.__self__ is struct
struct.pack_into(b'', 0, 1)
struct.unpack(struct.pack(1) + ' ') == (1,)
struct.unpack('x') == ()
struct.unpack(struct.pack(1) + ' ')[0] == 1
struct.format = "ii"
struct = _struct.Struct('p')
struct.unpack(struct.pack(False)) == (0,)
struct = _struct.Struct('b')
struct.unpack(struct.pack(True)) == (-1,)
struct = _struct.Struct('?')
struct.unpack(struct.pack(True)) == (True,)
struct = _struct.Struct('
