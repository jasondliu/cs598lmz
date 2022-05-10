import ctypes
# Test ctypes.CFUNCTYPE'ed callback, with multiple argtypes
lib = CDLL(get_filename("cfn_callbacks_argtypes.#"))

prototype = CFUNCTYPE(c_int, c_char, c_int, c_double)
def myfunc(*args):
    global state
    state += 1
    return len(args)

lib.test.restype = c_int
lib.test.argtypes = [prototype]

state = 0
assert lib.test(myfunc) == 2
assert state == 3

# Repeat with structs
lib = CDLL(get_filename("cfn_callbacks_argtypes.#"))
class Point(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]

prototype = CFUNCTYPE(None, Point, Point)
def myfunc(*args):
    global state
    state += 1
    return len(args)

lib.test.restype = c_int
lib.test.argtypes = [prototype]

state = 0
assert lib.test(myfunc) == 1

