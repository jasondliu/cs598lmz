import _struct
# Test _struct.Struct.format
print("_struct.Struct")
print("--------------")
print("format")

################################################################################
# Basic format tests
#

def check(input, expect):
    binsz = size(input)
    print("format:", input, binsz)
    s = Struct(input)
    assert s.format == input
    assert s.size == binsz
    assert s.unpack("") == ()

assert 3 == size("<cAhH")

# check("c", 1)
# check("?", 1)
# check("B", 1)
# check("b", 1)
# check("h", 2)
# check("H", 2)
check("i", 4)
# check("I", 4)
# check("l", 4)
# check("f", 4)
# check("d", 8)
# check("L", 8)
# check("q", 8)
# check("Q", 8)

# Check that passing in a bad format string raises a ValueError
# try:
#     check("X")
# except ValueError:
#    
