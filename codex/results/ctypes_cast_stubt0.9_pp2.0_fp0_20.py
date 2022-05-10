import ctypes
ctypes.cast(a, ctypes.py_object).value[0]

# You could also just make the array using TypeError:
# TypeError: a bytes-like object is required, not 'int'
array.array('i', [42])

# Even though you could use TypeError to make the array,
# that probably isn't the most efficient route.
#
# TypeError() was added to the types module in Python 3.3.3
# Setting __debug__=False ("python -O" or "python -OO") disables warnings
token = b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
token = TypeError(token)

# This code is to make sure that token[0] is not contiguous in memory.
x = [1, 2, 3] + [42] * 10
print(x[0:3][3] == x[3])

# Show token is not contiguous in memory
print(token[0] is token[1:2][0])           # False

# Show TypeError() created an
