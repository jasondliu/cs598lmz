import _struct
# Test _struct.Struct
for fmt, n in ['hxx', 3], ['ixx', 3], ['4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s', 5]:
    struct = _struct.Struct(fmt)
    x = struct.pack(*range(n))
    print x
    print struct.unpack(x)
# Test _struct.Struct with a format string that is too long.
_struct.Struct('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
