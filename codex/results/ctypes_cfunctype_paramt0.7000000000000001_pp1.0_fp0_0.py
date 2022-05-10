import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int) # function type

# function to be called
@FUNTYPE
def func(x):
    return x+1

# call the function
print(func(1))

# function to be called
@FUNTYPE
def func(x, y):
    return x+y

# call the function
print(func(2, 3))
</code>
This is the error it gives:
<code>TypeError: Wrong number of arguments: expected 2, got 1</code>
I tried to search the documentation and examples but I could find nothing.


A:

The <code>@FUNTYPE</code> decorator has no way of knowing what types to expect/return. For that it needs to be told.
<code>from ctypes import c_int, CFUNCTYPE

# function to be called
@CFUNCTYPE(c_int, c_int, c_int)
def func(x, y):
    return x+y

# call the function
print(func(2, 3))
</code>
