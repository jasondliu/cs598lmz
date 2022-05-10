from types import FunctionType
list(FunctionType(lambda x: x, {}).__globals__.keys())

# [Out]:
# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', '__builtin_module_names']

# 可以看到 __builtins__ 是存在的，并且是一个字典

# 另外，__builtins__ 并不是一个模块，而是一个字典，所以不能像导入模块一样导入它

# 在 Python 3 中，__builtins__ 是一个模块，可以直接导入

# 在 Python 3 中，__builtins__
