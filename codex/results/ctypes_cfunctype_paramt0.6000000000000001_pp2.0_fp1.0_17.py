import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

# Define a function in Python.
def f(x, y):
    return x + y

# Register this function in the library.
register_function("f", FUNTYPE(f))

# Call the function from C++.
print(library.f(1.0, 2.0))

# Unregister the function.
unregister_function("f")

# Register a new function.
def g(x, y):
    return x * y

register_function("g", FUNTYPE(g))

# Call the new function from C++.
print(library.g(1.0, 2.0))

# Unregister the function.
unregister_function("g")
</code>
<code>library.h</code>:
<code>#ifndef LIBRARY_H
#define LIBRARY_H

#include &lt;pybind11/pybind11.h&gt;
#include &lt;pybind11/functional.h&gt;
