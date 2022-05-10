from types import FunctionType
list(FunctionType(lambda x: x, {}).__globals__.keys())

# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', '__builtin_module_names']

# 但是，如果我们把__builtins__放到全局命名空间里，就可以访问到了

def f():
    pass

f.__globals__['__builtins__'] = __builtins__

# 如果你想要把一个函数的全局命名空间完全清空，可以这样做

def f():
    pass

f.__globals__.clear()

#
