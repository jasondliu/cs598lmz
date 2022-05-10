import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "in python callback", a, b
    return a + b

CALLBACK = FUNTYPE(my_callback)

# Create an instance of MyClass
my_class = MyClass()

# Call a method of the class that takes a callback
my_class.call_me_back(CALLBACK)
