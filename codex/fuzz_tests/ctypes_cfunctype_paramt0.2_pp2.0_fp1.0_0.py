import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "my_callback was called with %d, %d" % (a, b)
    return a + b

my_callback = FUNTYPE(my_callback)

# Create a new C++ instance of the class
my_obj = MyClass(my_callback)

# Call a method of the class
my_obj.call_me(2, 3)
</code>

