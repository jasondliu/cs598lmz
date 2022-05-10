from types import FunctionType
list(FunctionType(lambda:0,{}).__globals__.keys())

#['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', '__builtin_module_names__']

# 可以看到，除了__builtins__这个内置模块之外，其他的都是自定义的

# 可以看到，__builtins__是一个dict，里面存放了Python内置的各种对象，这些对象在各个模块中都可以直接使用

# 如果要查看Python源码
