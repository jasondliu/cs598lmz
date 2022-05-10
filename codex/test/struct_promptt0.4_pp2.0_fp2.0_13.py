import _struct
# Test _struct.Struct.format_size

# This tests the format_size method of the Struct class.
# It checks that the size of the format string is correct.

import _struct

# This test uses the following format strings:
#
#   'x'       1 byte
#   'c'       1 byte
#   'b'       1 byte
#   'B'       1 byte
#   '?'       1 byte
#   'h'       2 bytes
#   'H'       2 bytes
#   'i'       4 bytes
#   'I'       4 bytes
#   'l'       4 bytes
#   'L'       4 bytes
#   'q'       8 bytes
#   'Q'       8 bytes
#   'f'       4 bytes
#   'd'       8 bytes
#   's'       1 byte per character
#   'p'       1 byte per character
#   'P'       4 bytes

# The following list contains the size of the format string.
# It is used to test the size of the format string.

