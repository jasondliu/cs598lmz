import ctypes
# Test ctypes.CFUNCTYPE with an empty argtype list.
import _ctypes
#
# This tests the case where the function takes no arguments.
#
def func():
    return 42

try:
    FUNC_TYPE = ctypes.CFUNCTYPE(ctypes.c_int)
except TypeError:
    raise SystemExit

f = FUNC_TYPE(func)
assert f() == 42
assert f.__name__ == "func"

# test that this works with a function not in the globals()
def func2():
    return func()

f = FUNC_TYPE(func2)
assert f() == 42
assert f.__name__ == "func2"

# test that this works with a function not in the globals()
# and with a default argument
def func3(a=1):
    return func() + a

f = FUNC_TYPE(func3)
assert f() == 43
assert f.__name__ == "func3"

# test that this works with a function not in the globals()
# and with a default argument
def func4(
