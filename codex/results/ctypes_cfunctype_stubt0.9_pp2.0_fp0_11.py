import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return u'\xe2\x9c\xbee'

# This should raise an error during setup
ctypes.cdll.LoadLibrary(ctypes.util.find_library('c')).\
                  get_errno.argtypes = [c_int, c_int]
# This should raise an error during invocation,
# but is already caught in test_submodule2
fun
# Make sure that the interpreter finalizes correctly.
ctypes.string_at(0)
