from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(type(a) == type(b))
print(isinstance(a, type(b)))
print(type(a) == FunctionType)

# 不可变类型
# 字符串，数值，元组
# 可变类型
# 列表，字典，集合

a = [1, 2, 3]
b = a
print(a is b)
print(a == b)
a[0] = 10
print(a)
print(b)
print(a is b)
print(a == b)

# 切片
a = [1, 2, 3]
b = a[:]
print(a is b)
print(a == b)
a[0] = 10
print(a)
print(b)
print(a is b)
print(a ==
