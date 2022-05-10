import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

import ctypes
import ctypes.util
lib = ctypes.util.find_library('m')
if lib: tests.append(lib)
else: lib = ctypes.cdll.msvcrt # so it doesn't crash, at least

################################################################

from test import test_support
test_support.run_unittest(test_main(tests, True))
