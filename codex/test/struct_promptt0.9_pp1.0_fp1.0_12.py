import _struct
# Test _struct.Struct implementation
def pack_byteorder(fmt):
    s = _struct.Struct(fmt)
    if s.size < 5:
        return pack_byteorder(fmt + 'x')
    for byteorder in '@=<>!':
        for fmt2 in (fmt + byteorder, byteorder + fmt):
            s2 = _struct.Struct(fmt2)
            yield fmt2, byteorder, s2.size
register_checker(pack_byteorder,
                 arg_count=1, arg_types=(str,),
                )

# Test _struct.Struct.iter_unpack
def iter_unpack_contents(data, fmt):
    s = _struct.Struct(fmt)
    return list(s.iter_unpack(data))
register_checker(iter_unpack_contents,
                 arg_types=(bytes, str), arg_counts=(2,),
                )

def iter_unpack_with_buffer(data, fmt):
    s = _struct.Struct(fmt)
