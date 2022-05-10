import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "my_callback was called with %d and %d" % (a, b)
    return a + b

my_callback = FUNTYPE(my_callback)

lib.register_callback(my_callback)

print "Calling C function"
print "return value: %d" % lib.call_callback()
</code>
The output is:
<code>Calling C function
my_callback was called with 1 and 2
return value: 3
</code>

