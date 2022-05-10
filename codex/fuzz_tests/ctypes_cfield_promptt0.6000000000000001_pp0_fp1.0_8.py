import ctypes
# Test ctypes.CField.
# This is used by the parser to represent a single field in a structure or union.
# It has the following members:
#   name: the name of the field
#   type: the type of the field
#   offset: the offset of the field within the structure or union
#   bitsize: the size of the field in bits
#   bitoffset: the offset of the field within the first byte containing data
#   flags: a bitmask of flags
#   ctype: a ctypes._SimpleCData subclass representing the field's type
#
# ctypes.CField inherits from ctypes._CData and supports the following methods:
#   __repr__: return a string representation of the field
#   in_dll: return a ctypes object representing the field
#
# ctypes.CField objects support the following attributes:
#   in_dll: same as the method
#   value: the value of the field
#   address: the address of the field
#   _objects: the ctypes object containing the field

# This test depends on the ctypes test_structures module.
import test.test_
