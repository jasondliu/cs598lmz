import _struct
# Test _struct.Struct.format_size()

# This is a list of all possible format characters
# (except 'x', which is not implemented)
# For each one, we test a structure with one member.
# We also test '@' and '=' as well as '<', '>', and '!'
# (for native, network, and standard byte order).
#
# The test is to check that the size of the structure
# is correct, and that the format string is correct.

# The size of the structure is the size of the member
# (as returned by the calcsize() function)
# plus any alignment padding.

# The format string is the format character,
# followed by a number (the size of the member),
# followed by an optional 's' (if the member is a string)
# followed by an optional 'p' (if the member is a pascal string)
# followed by an optional 'P' (if the member is a pascal string)
# followed by an optional '?' (if the member is a bit field)
# followed by an optional '!' (if the member is a bit field)
#
