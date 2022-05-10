from types import FunctionType
list(FunctionType(lambda x: x, {}).__globals__.keys())

# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', '__builtin_module_names__']

# 可以看到，__builtins__ 是一个 dict，里面有很多内置函数，可以直接使用。

# 如果我们要添加自己的全局变量，可以直接修改 __builtins__ 的值：

FunctionType(lambda x: x, {}).__globals__['print']('hello world')

# hello world

# 但是这种方法并不
