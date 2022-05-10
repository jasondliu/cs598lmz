import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("in python callback", a, b)
    return a + b

callback = FUNTYPE(my_callback)

# Create a new instance of the class
my_obj = MyClass(callback)

# Call the instance method
my_obj.call_me(1, 2)
</code>
The output is:
<code>in python callback 1 2
3
</code>

