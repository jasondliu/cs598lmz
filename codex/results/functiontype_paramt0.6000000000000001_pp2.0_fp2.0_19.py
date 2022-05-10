from types import FunctionType
list(FunctionType(f.__code__, globals(), 'f')() for f in [lambda: 2, lambda x: 3, lambda x, y: 4])

# from types import FunctionType
# list(FunctionType(f.__code__, globals(), 'f')() for f in [lambda: 2, lambda x: 3, lambda x, y: 4])

# list(FunctionType(f.__code__, globals(), 'f')() for f in [lambda: 2, lambda x: 3, lambda x, y: 4])

# list(FunctionType(f.__code__, globals(), 'f')() for f in [lambda: 2, lambda x: 3, lambda x, y: 4])

# def f(x):
#     return x + x

# f(2)

# def f(x):
#     return x + x

# f(2)

# def f(x):
#     return x + x

# f(2)

# def f(x):
#     return x + x

# f(2)

# def
