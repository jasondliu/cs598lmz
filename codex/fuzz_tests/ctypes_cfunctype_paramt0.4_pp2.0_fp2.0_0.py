import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Define a function with the above prototype
def my_func(x, y):
    return x+y

# Cast the function to the prototype
f = FUNTYPE(my_func)

# Call the function
print(f(1,2))

# Or, if you prefer, you can use a decorator
@FUNTYPE
def my_func(x, y):
    return x+y

print(my_func(3,4))
</code>

