import ctypes
# Test ctypes.CField
#
# This example shows how to use the ctypes.CField class to create
# a C structure that contains a bit field.
#
# The 'short' type is used, so the bit field is at most 16 bits wide.
#
# The CField class is used to create the 'a' and 'b' fields.
# The 'a' field is 4 bits wide, the 'b' field is 5 bits wide.
# The 'c' field is not defined using CField, but it is still
# a bit field. The 'c' field is 7 bits wide.
#
# The 'd' field is not a bit field, it is a regular integer field.
#
# The 'e' field is a bit field, but it is not defined using CField.
# The 'e' field is 16 bits wide.
#
# The 'f' field is not a bit field, it is a regular integer field.
#
# The 'g' field is a bit field, but it is not defined using CField.
# The 'g' field is 16 bits wide.
#
# The 'h' field is not
