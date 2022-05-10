import ctypes
# Test ctypes.CFUNCTYPE

from foo import *

# Check that we can pass a CFUNCTYPE instance to a C function as an argument
p = POINTER(c_int)

i = c_int.in_dll(foo, "i")
assert i.value == 1
passthru = CFUNCTYPE(None, p)(("passthru", foo), ((1,),))
passthru(byref(i))
assert i.value == 2

# Check that we can take a pointer to a CFUNCTYPE instance and pass it
# as an argument to a C function.
my_func = CFUNCTYPE(c_int, c_int)(lambda num: num * 3)
with pytest.raises(TypeError):
    # The c_int.in_dll function doesn't accept a c_void_p rather than an int
    addr = c_int.in_dll(foo, "passthru")._as_parameter_
foo.set_callback(addr, byref(my_func))
assert my_func(10) == 30
assert foo.call
