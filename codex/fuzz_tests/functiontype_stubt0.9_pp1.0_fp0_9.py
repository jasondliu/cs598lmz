from types import FunctionType
a = (x for x in [1])
type(a)

d = {1:1}

#内置函数
print(callable(print))
print(callable(a))
print(callable(d))
print(callable(function_test))
print(callable(FunctionType))
print(callable(lambda x:x))
