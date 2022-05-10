import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

obj = S.x
print(type(obj))
print(obj)
print(obj.__dict__)
print(obj.__class__)

# __doc__
# __init__
# __module__
# _type_
# _name_
# _offset_
# _size_
# _pack_
# _index_
# _length_
# _alignment_
# _ctype_
# _is_array_
# _is_packed_
# _is_pointer_
# _is_void_
# _is_simple_
# _is_bitfield_
# _is_struct_
# _is_union_
# _is_fundamental_
# _is_integer_
# _is_float_
# _is_pointer_
# _is_array_
# _is_scalar_
# _is_char_
# _is_byte_
# _is_native_
# _is_signed_
# _is_unsigned_
# _is_short_
# _is_long_
# _is
