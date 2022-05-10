import _struct
# Test _struct.Struct from builtins python module
# https://docs.python.org/3.8/library/struct.html
# Struct('<'): little-endian
# Struct('>'): big-endian
# The body of structs is described by the format string.
# Format codes c, b, B and ? are signed, such that packing -1 yields the same
# result as packing 255
# The format string '<HQ' signifies: a little-endian unsigned short int & a
# little-endian unsigned long long int
# unpacking = retrieving the values in the struct again
def test_struct():
    test_list = [0x1234, 0x567898763456]
    test_string = _struct.Struct('<iQ').pack(*test_list)
    unpacked_list = _struct.Struct('<iQ').unpack(test_string)
    assert test_list == list(unpacked_list)
