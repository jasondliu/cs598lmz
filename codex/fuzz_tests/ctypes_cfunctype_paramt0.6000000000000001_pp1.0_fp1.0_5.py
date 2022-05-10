import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Set up the prototype for the user's function.
# This is a hack to allow the user to define their function in the top level
# namespace.
def f(x):
    if x < 0:
        raise ValueError("x must be non-negative")
    return x * x

def callback(x):
    return f(x)

# Wrap the user's function as a C callback function.
callback_func = FUNTYPE(callback)

# Define the C function.
_cubic = _cubic_lib.cubic
_cubic.argtypes = [FUNTYPE]
_cubic.restype = ctypes.c_double

# Call the C function.
_cubic(callback_func)

# Output:
#   14.0
```

## Converting C++ code to Python

The `cpp2py_lib` module contains the Python wrapper code for the C++
library.

```python
>>> import cpp2py_lib
>>> cpp
