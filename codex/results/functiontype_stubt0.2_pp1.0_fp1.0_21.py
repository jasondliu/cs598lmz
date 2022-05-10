from types import FunctionType
a = (x for x in [1])
b = [1,2,3]
c = {1:2,3:4}
d = {1,2,3}
e = FunctionType
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# 判断一个对象是否是函数
print(callable(a))
print(callable(b))
print(callable(c))
print(callable(d))
print(callable(e))

# 判断一个对象是否是可迭代对象
print(isinstance(a,Iterable))
print(isinstance(b,Iterable))
print(isinstance(c,Iterable))
print(isinstance(d,Iterable))
print(isinstance(e,Iterable))

# 判断一个对象是否是迭代器
print(isinstance(a,
