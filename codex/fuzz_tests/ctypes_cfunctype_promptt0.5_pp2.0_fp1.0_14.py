import ctypes
# Test ctypes.CFUNCTYPE

# This is the prototype of the callback function
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def test(a, b):
    print "test", a, b
    return a + b

# Convert the Python function to a C callback
callback = prototype(test)
# Call the C function, which will call the Python function
print callback(1, 2)

# The following will fail because the callback has the wrong signature
def test(a):
    print "test", a
    return a

try:
    callback = prototype(test)
except TypeError:
    print "Failed"
else:
    print "Succeeded"

# Test ctypes.WINFUNCTYPE

# This is the prototype of the callback function
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)

def test(a, b):
    print "test", a, b
    return a + b

# Convert the Python function to a C callback
callback = prototype
