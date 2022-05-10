from types import FunctionType
list(FunctionType(lambda:0,{}).__globals__.keys())

# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', '__builtin_module_names']

# 可以看到，__builtins__是一个模块对象，这个模块对象里面包含了Python的所有内置函数，我们可以直接访问这个模块对象的属性来调用内置函数

# FunctionType(lambda:0,{}).__globals__['__builtins__'].abs(-1)

# 1

# 因此，
