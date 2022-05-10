from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# [1]

# [2]

def f(x):
    return x
list(FunctionType(f.__code__, globals(), 'f'))

# [2]

# [3]

def f(x):
    return x
list(FunctionType(f.__code__, globals(), 'f'))

# [3]

# [4]

def f(x):
    return x
list(FunctionType(f.__code__, globals(), 'f'))

# [4]

# [5]

def f(x):
    return x
list(FunctionType(f.__code__, globals(), 'f'))

# [5]

# [6]

def f(x):
    return x
list(FunctionType(f.__code__, globals(), 'f'))

# [6]

# [7]

def f(x):
    return x
list(FunctionType(f.__code
