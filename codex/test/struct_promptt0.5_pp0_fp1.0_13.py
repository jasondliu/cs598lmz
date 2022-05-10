import _struct
# Test _struct.Struct.
import _struct

def test_struct(module, s, format, expected):
    # Test the struct object.
    if module.calcsize(format) != len(expected):
        raise ValueError("invalid calcsize()")
    s1 = module.Struct(format)
    if s1.size != len(expected):
        raise ValueError("invalid size")
    if s1.format != format:
        raise ValueError("invalid format")
    s2 = module.Struct(format)
    if s1.format != s2.format:
        raise ValueError("invalid format")
    if s1.size != s2.size:
        raise ValueError("invalid size")
    # Test the pack() method.
    if s1.pack(*s1.unpack(expected)) != expected:
        raise ValueError("invalid pack()")
    if s1.pack(s1.unpack(expected)[0]) != expected:
        raise ValueError("invalid pack()")
