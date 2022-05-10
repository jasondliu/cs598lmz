import _struct
# Test _struct.Struct

# Map spec chars to unpackers
std_specs = {
    b'x': lambda s, p: (b'', p + 1),
    b'c': _struct.Struct._unpack_c,
    b'b': _struct.Struct._unpack_b,
    b'B': _struct.Struct._unpack_B,
    b'h': _struct.Struct._unpack_h,
    b'H': _struct.Struct._unpack_H,
    b'i': _struct.Struct._unpack_i,
    b'I': _struct.Struct._unpack_I,
    b'l': _struct.Struct._unpack_l,
    b'L': _struct.Struct._unpack_L,
    b'q': _struct.Struct._unpack_q,
    b'Q': _struct.Struct._unpack_Q,
    b'n': _struct.Struct._unpack_n,
    b'N': _struct.Struct._unpack_N,
    b'e': _struct.Struct._un
