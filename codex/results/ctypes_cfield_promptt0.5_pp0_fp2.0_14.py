import ctypes
# Test ctypes.CField

# This is a list of all the types that should be checked.
# If you add a new type to ctypes, add it here.
#
# The list is a list of tuples, each tuple contains:
# - the type to check
# - an object of the type
# - the expected c_type attribute
# - the expected c_size attribute
# - the expected c_alignment attribute
# - the expected c_name attribute
# - the expected c_pack attribute

import struct
import sys

# test ctypes.CField

TestTypes = [
    (ctypes.c_byte, ctypes.c_byte(42),
     ctypes.c_byte, 1, 1, "c_byte", 1),

    (ctypes.c_ubyte, ctypes.c_ubyte(42),
     ctypes.c_ubyte, 1, 1, "c_ubyte", 1),

    (ctypes.c_short, ctypes.c_short(42),
     ctypes.c_short, 2, 2, "c_short", 1
