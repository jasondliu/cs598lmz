import ctypes
ctypes.cast(id(0), ctypes.py_object).value

# displays the address of the object in memory
id(1)

# is the same as
ctypes.cast(id(1), ctypes.py_object).value

# this is how a function is defined
def square(x):
    return x * x

# this is how you get the address of the function
id(square)

# and this is how you get the object at that address
ctypes.cast(id(square), ctypes.py_object).value

# which is the function object
type(ctypes.cast(id(square), ctypes.py_object).value)

# this is how you call the function
square(2)

# this is how you access the function's __code__ attribute
square.__code__

# this is how you get the address of the code object
id(square.__code__)

# and this is how you get the object at that address
ctypes.cast(id(square.__code__), ctypes.py_object).value

# which is the
