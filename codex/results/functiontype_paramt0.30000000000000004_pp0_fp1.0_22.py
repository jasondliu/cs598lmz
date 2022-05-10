from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), 'foo'))

# TypeError: 'function' object is not iterable

# The function type is not a sequence, so it does not support iteration.
#  The __iter__() method is not defined for functions.

# However, the function type does support the __getitem__() method, so you can access individual characters in the function’s name.

FunctionType(lambda x: x + 1, globals(), 'foo')[0]

# 'f'

# The function type also supports the __len__() method, so you can find out how long the function’s name is.

len(FunctionType(lambda x: x + 1, globals(), 'foo'))

# 3

# The __getitem__() and __len__() methods are defined for functions because they are defined for code objects, which are the underlying objects that represent Python functions.

# A code object is a sequence of bytes that represents the compiled version of a function body.

# You can get the code object for a function by accessing its __code__ attribute.


