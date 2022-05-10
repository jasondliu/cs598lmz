from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == FunctionType)
print(type(a) is FunctionType)

# 生成器表达式
a = sum(x for x in range(10))
print(a)

# 列表推导式
a = [x for x in range(10)]
print(a)

# 字典推导式
a = {x: x for x in range(10)}
print(a)

# 集合推导式
a = {x for x in range(10)}
print(a)

# 字典推导式
a = {x: x for x in range(10)}
print(a)

# 字典推导式

