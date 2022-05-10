import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

#
# This is the callback function that we'll pass to the C function.
#
def my_callback(a):
    print "my_callback called with %d" % a
    return a

#
# This is the C function that takes a callback.
#
def call_callback(callback):
    return callback(42)

#
# This is the Python wrapper for the C function.
#
@FUNTYPE
def call_callback_wrapper(callback):
    return call_callback(callback)

#
# This is the C function that takes a callback.
#
def call_callback_with_arg(callback, arg):
    return callback(arg)

#
# This is the Python wrapper for the C function.
#
@FUNTYPE
def call_callback_with_arg_wrapper(callback, arg):
    return call_callback_with_arg(callback, arg)

#
# This is the Python wrapper for the C function.
#
@FUNTYPE
def call_callback_with_arg_wrapper
