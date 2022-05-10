import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(a):
    print("callback called with:", a)
    return a

my_callback_c = FUNTYPE(my_callback)

# create a new C++ instance of MyClass
my_class = MyClass()

# call the C++ method
my_class.call_me(my_callback_c)
</code>

