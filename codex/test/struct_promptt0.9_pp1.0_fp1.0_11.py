import _struct
# Test _struct.Struct being used by both optimized and unoptimized functions
# Various use patterns are covered here.
# Check for structs with endianers prefixing the format string
little_endian_test_struct = _struct.Struct('<ii')
big_endian_test_struct = _struct.Struct('>ii')
native_endian_test_struct = _struct.Struct('ii')
native_endian_test_struct_ptr_size = _struct.Struct('pp')
little_endian_test_struct_int = _struct.Struct('<i')
big_endian_test_struct_int = _struct.Struct('>i')
native_endian_test_struct_int = _struct.Struct('i')

def unoptimised_pack(*args):
    # Add padding to test pack_into and unpack_from results.
    pad_bfr = 'P'
    fmt = 'ii'
    fmt = pad_bfr*3 + fmt
    fmt = fmt + pad_bfr*3
    # Call pack directly and not via the generated method pack_xx, since the
   
