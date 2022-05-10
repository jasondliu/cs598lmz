from types import FunctionType
list(FunctionType(lambda:1).__globals__.keys())

# {'__name__',
#  '__doc__',
#  '__package__',
#  '__loader__',
#  '__spec__',
#  '__annotations__',
#  '__builtins__',
#  '__file__',
#  '__cached__',
#  '__builtin_module_names__'}

# 函数的 __globals__ 属性是一个字典，它包含了定义函数时可用的全局变量。
# 这个字典是只读的，且不会更新
# 当程序执行时，它指向当前模块的全局变量字典
# 如果在
