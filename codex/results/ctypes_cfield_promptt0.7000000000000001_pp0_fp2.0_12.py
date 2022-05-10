import ctypes
# Test ctypes.CField.
#
# CFields are used to indicate that a particular field of a C struct is
# located at a fixed offset, rather than at an offset that depends on
# other fields.
#
# These are often used for bit fields, but can also be used to force
# particular fields to be aligned to the beginning of a struct.
#
# In either case, the offset from the beginning of the struct to the
# field is fixed, and can be specified as a keyword argument to CField.
#
# The syntax of CField is as follows:
#
# CField(name, type, offset=offset)
#
# name is the name of the field, and type is its type.
#
# If the field is a bit field, then type is a tuple:
# (type, size_in_bits, pack_flag)
#
# pack_flag is one of '<' or '>', and indicates whether the field
# is packed from the least significant to the most significant bit,
# or vice versa.
#
# In the following test, we check that CFields are properly defined
# for bit fields.
