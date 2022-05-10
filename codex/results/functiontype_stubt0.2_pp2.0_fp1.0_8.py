from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == FunctionType)
print(type(a) is FunctionType)
print(type(a) == type(b) == FunctionType)
print(type(a) is type(b) is FunctionType)

# 列表推导式
print([x for x in [1, 2, 3]])
print([x for x in [1, 2, 3] if x % 2 == 0])
print([x if x % 2 == 0 else '奇数' for x in [1, 2, 3]])
print([x for x in [1, 2, 3] if x % 2 == 0 if x % 3 == 0])
print([x for x in [1, 2, 3] if x % 2 == 0 if x % 3 == 0 else '不能被2和3整除'])
