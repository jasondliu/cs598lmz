import ctypes
# Test ctypes.CFUNCTYPE(type, ...)
#
# Define a simple callback to be executed
def callback(arg):
    print "callback called"
    print "    arg:", arg
    return 17
#
# Define the prototype of the callback
CALLBACK = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
#
# Get a callback instance
cb = CALLBACK(callback)
#
# Execute it
value = cb(42)
print "callback returned", value
assert value == 17
