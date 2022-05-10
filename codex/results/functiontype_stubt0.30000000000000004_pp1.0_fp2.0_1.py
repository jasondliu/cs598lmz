from types import FunctionType
a = (x for x in [1])
b = [1,2,3]
c = {'a':1}
d = 'abc'
e = 123
f = FunctionType(lambda x:x,globals())
g = type(a)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

# 判断一个对象是否是函数
print(callable(f))

# 判断一个对象是否是可迭代对象
print(isinstance(a,Iterable))

# 判断一个对象是否是迭代器
print(isinstance(a,Iterator))

# 判断一个对象是否是生成器
print(isinstance(a,Generator))

# 判断一
