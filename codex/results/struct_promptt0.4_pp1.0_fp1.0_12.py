import _struct
# Test _struct.Struct()

import struct

def test_struct_format(format):
    # Test _struct.Struct() with the given format
    s = _struct.Struct(format)
    print(s)
    print(s.size)
    print(s.format)
    print(s.unpack_from)
    print(s.pack_from)
    print(s.unpack)
    print(s.pack)
    print(s.iter_unpack)
    print(s.iter_unpack_from)
    print(s.iter_unpack_dict)
    print(s.iter_unpack_dict_from)

    # Test pack/unpack
    data = s.pack(1, 2, 3)
    print(data)
    print(s.unpack(data))
    print(s.unpack_from(data))
    print(s.unpack_from(data, 0))
    print(s.unpack_from(data, 1))
    print(s.unpack_from(data, 2))
    print(s.un
