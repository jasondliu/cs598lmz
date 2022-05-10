import ctypes
# Test ctypes.CField and ctypes.CStruct function.

# In the list below, the comment "succeeds" means that the corresponding code
# prints "ok" when executed independently.  The comment "fails" means it does
# NOT print "ok" when executed independently.  The comment "compile only"
# means it prints nothing when executed independently, but doesn't crash or get
# an assertion failure.  All of this is trying to say that when these are listed
# as a single program, it should print "ok" in all cases.

# The first list is arranged in order of the fields from the REF_BASIC structure,
# the second list is in order of the fields from the REF_OLD structure, and the
# third list is in order of the fields from the REF_NEW structure.

from ctypes import *

# The 'C' list contains all types.  The 'c' list contains only 'c' types - it is
# used to verify that calling get_ctype_code() with an unsupported item throws
# an exception.

C = ['c', 'b', 'B', 'h',
