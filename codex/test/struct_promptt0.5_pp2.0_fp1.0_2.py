import _struct
# Test _struct.Struct.__new__()

import sys

# Test that the __new__() method of the Struct class returns an instance of
# the Struct class.
class StructSubclass(Struct):
    pass

try:
    s = StructSubclass('i')
except TypeError:
    print("SKIP")
    sys.exit()

print(type(s))
