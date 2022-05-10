import _struct
# Test _struct.Struct's format string
struct_test.test_struct()

#-------------------------------------------------------------------------------
import tracemalloc
# Test tracemalloc
tracemalloc_test.test_tracemalloc()

#-------------------------------------------------------------------------------
import random
# Test random
random_test.test_random()

#-------------------------------------------------------------------------------
import itertools
# Test itertools
itertools_test.test_itertools()

#-------------------------------------------------------------------------------
import hashlib
# Test hashlib
hashlib_test.test_hashlib()

#-------------------------------------------------------------------------------
import types
# Test types
types_test.test_types()

#-------------------------------------------------------------------------------
import zipimport
# Test zipimport
zipimport_test.test_zipimport()

#-------------------------------------------------------------------------------
import resource
# Test resource
resource_test.test_resource()

#-------------------------------------------------------------------------------
# Test contextlib
import contextlib
contextlib_test.test_contextlib()

#-------------------------------------------------------------------------------
# Test winreg
if sys.platform == "win32":
    import winreg
    winreg_test.test_winreg()

#-------------------------------------------------------------------------------
#
