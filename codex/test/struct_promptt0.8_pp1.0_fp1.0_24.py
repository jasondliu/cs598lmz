import _struct
# Test _struct.Struct
for fmt, n in ['hxx', 3], ['ixx', 3], ['4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s4s', 5]:
    struct = _struct.Struct(fmt)
