from types import FunctionType
list(FunctionType(lambda x: x, globals()))

# [<function <lambda> at 0x7f8e8d7c9a60>, <function <lambda> at 0x7f8e8d7c9b90>]

# 上面的代码中，FunctionType()函数的第一个参数是一个函数对象，第二个参数是一个字典，
# 这个字典是函数对象的全局变量。

# 可以通过FunctionType()函数创建函数对象，但是这个函数对象不能直接调用，需要使用MethodType()函数创建方法对象。
