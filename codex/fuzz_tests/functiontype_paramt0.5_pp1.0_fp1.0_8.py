from types import FunctionType
list(FunctionType(lambda: 1))

# TypeError: 'function' object is not iterable
# FunctionType(lambda: 1).__iter__()

# TypeError: 'function' object is not iterable
# iter(FunctionType(lambda: 1))

# TypeError: 'function' object is not iterable
# FunctionType(lambda: 1).__next__()

# TypeError: 'function' object is not iterable
# next(FunctionType(lambda: 1))

# TypeError: 'function' object is not iterable
# FunctionType(lambda: 1).__contains__(1)

# TypeError: 'function' object is not iterable
# 1 in FunctionType(lambda: 1)

# TypeError: 'function' object is not iterable
# FunctionType(lambda: 1).__getitem__(0)

# TypeError: 'function' object is not iterable
# FunctionType(lambda: 1)[0]

# TypeError: 'function' object is not iterable
# FunctionType(lambda: 1).__len__()

# TypeError: 'function' object
