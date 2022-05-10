import ctypes
ctypes.cast(3, ctypes.py_object)

# Some common operations
a << 2                  # a shifted left two bits
a | b                   # bits set in either a or b
a & b                   # bits set in both a and b
a ^ b                   # bits set in a or b but not both
a & ~ b                 # bits set in a but not in b

a == b                  # True if a and b have the same value
a != b                  # True if a and b have different values
b + 1 == a              # True if b is a predecessor of a
a - b == 1              # True if b is a predecessor of a
a > b                   # True if a is greater than b

# Other tests
a and b                 # b if a is false, else a
a or b                  # a if a is true, else b
not a                   # True if a is false, False if a is true

# Identity tests
a is b                  # True if a and b are the same object
a is not b              # False if a and b are the same object

# Functions to create and destroy objects
type(obj
