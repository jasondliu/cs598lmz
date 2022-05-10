import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int32)

# We need to create a python function as an argument to the C++ library
# What we are doing here is creating a Python function that takes in a string
# called x, and returns nothing.
def foo(x):
  print("Hello pybind11!\n")

# Now create a Python function that takes in 3 arguments, x, y and z,
# where x and y are of type long (int64 in python3), z is of type FUNTYPE,
# which is a C++ function pointer, defined by the third argument.
# And return a long (int64 in python3)
@pybind11.cpp_function
@pybind11.returns(long)
def add(x, y, z):
  pass

# Create a Python variable add_py which is the Python implementation of add().
# Here the first argument comes from C++, the second argument is always 'None' (TODO),
# the third argument is the function 'foo', which is also from C++.
add_py = add(1, None, foo)

# Assert that
