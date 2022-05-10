from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__)==FunctionType)
print(type(a.__next__)==FunctionType)
# 循环一次后消失
print(next(a))
print(next(a))
print(next(a))
