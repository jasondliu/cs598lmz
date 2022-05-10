import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback called with %d and %d" % (a, b))
    return a + b

my_callback_c = FUNTYPE(my_callback)

# Create a new C++ instance of MyClass
my_class = MyClass()

# Set the callback function
my_class.set_callback(my_callback_c)

# Call a C++ function that executes the callback
my_class.execute_callback(1, 2)

# Delete the C++ instance
del my_class
</code>

