import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is the callback function
def py_func(a, b):
    print "Python function called with %d and %d" % (a, b)
    return a + b

# Convert the Python callback function into C callback
c_func = FUNTYPE(py_func)

# Call the C function with the C callback
print "Calling C function"
print "Return value is %d" % lib.c_func(2, 3, c_func)
</code>
Result:
<code>Calling C function
Python function called with 2 and 3
Return value is 5
</code>

