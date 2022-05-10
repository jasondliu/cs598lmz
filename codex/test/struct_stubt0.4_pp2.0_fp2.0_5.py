from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)
s.unpack(s.pack(1))
s.unpack_from(s.pack(1), 0)
s.size
s.format
s.format_size
s.pack_into(b'', 0, 1)
s.unpack_from(b'', 0)

import _struct
_struct.Struct.__new__(_struct.Struct)
_struct.Struct.__new__(_struct.Struct, 'i')
_struct.Struct.__new__(_struct.Struct, 'i').pack(1)
_struct.Struct.__new__(_struct.Struct, 'i').unpack(s.pack(1))
_struct.Struct.__new__(_struct.Struct, 'i').unpack_from(s.pack(1), 0)
_struct.Struct.__new__(_struct.Struct, 'i').size
_struct.Struct.__new__(_struct.Struct, 'i').format
_struct.Struct.__new__(_struct.Struct, 'i').format_size
