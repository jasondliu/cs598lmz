import ctypes
# Test ctypes.CFUNCTYPE()

# This is a function that takes a function pointer as an argument
# and calls it.

# The function pointer should take an int and return an int.

# This is the function we will pass to the test function.
def func(i):
    return i + 1

# This is the function pointer type we will use.
CFUNCTYPE(c_int, c_int)

# This is the function we will call.
test = cdll.msvcrt.test
test.argtypes = [CFUNCTYPE(c_int, c_int)]
test.restype = c_int

# Call it.
result = test(func)

# Check the result.
if result == func(0):
    print("It works!")
else:
    print("Something is wrong.")

# This is the function we will pass to the test function.
def func(i):
    return i + 1

# This is the function pointer type we will use.
CFUNCTYPE(c_int, c_int)

# This is the function we
