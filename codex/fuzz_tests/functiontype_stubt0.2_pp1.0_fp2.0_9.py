from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == FunctionType)
print(type(a) is FunctionType)

# 列表生成式
print([x for x in range(10)])
print([x for x in range(10) if x % 2 == 0])
print([x if x % 2 == 0 else -x for x in range(10)])
print([x for x in range(10) if x % 2 == 0 if x % 3 == 0])
print([x for x in range(10) if x % 2 == 0 if x % 3 == 0 if x % 5 == 0])
print([x for x in range(10) if x % 2 == 0 if x % 3 == 0 if x % 5 == 0 if x % 7 == 0])
print([x for x in range(10) if x % 2 ==
