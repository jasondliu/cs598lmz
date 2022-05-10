import ctypes
# Test ctypes.CFUNCTYPE
# https://docs.python.org/3/library/ctypes.html#ctypes.CFUNCTYPE
# The function that is called by the callback is specified by a
# callback function prototype.
# The prototype is a class derived from the ctypes.CFUNCTYPE
# class, specifying the number and type of arguments and the
# return type of the function. For example, a prototype of a
# callback function receiving an integer parameter and
# returning None is created as follows:

# def my_callback(i):
#     print("called back with", i)

# callback = CFUNCTYPE(None, c_int)(my_callback)

# The first argument to the CFUNCTYPE constructor is the return type of the function.
# If the function returns a simple type, you can use the corresponding ctypes type,
# such as c_int or c_float. If it returns a structure, you must create a class
# representing the structure.
# The second argument is a tuple containing the argument types.
# The callback function is called with the same arguments you pass to the callback
# function
