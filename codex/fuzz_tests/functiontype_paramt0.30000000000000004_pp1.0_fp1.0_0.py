from types import FunctionType
list(FunctionType(lambda: None, {}).__globals__.keys())

# list(FunctionType(lambda: None, {}).__globals__.values())

# list(FunctionType(lambda: None, {}).__globals__.items())

# def f():
#     pass
#
# f.__globals__

# def f():
#     pass
#
# f.__globals__['__builtins__']

# def f():
#     pass
#
# f.__globals__['__builtins__']['__import__']

# def f():
#     pass
#
# f.__globals__['__builtins__']['__import__']('os')

# def f():
#     pass
#
# f.__globals__['__builtins__']['__import__']('os').system('ls')

# def f():
#     pass
#
# f.__globals__['__builtins__']['__import__']('os').system('ls')
