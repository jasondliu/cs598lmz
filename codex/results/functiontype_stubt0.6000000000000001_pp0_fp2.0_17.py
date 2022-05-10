from types import FunctionType
a = (x for x in [1])
b = [1]
c = {1:2}
d = 1
e = FunctionType(lambda x:x, {})
print(type(a), type(b), type(c), type(d), type(e))

print(isinstance(a, Iterator), isinstance(b, Iterator), isinstance(c, Iterator), isinstance(d, Iterator), isinstance(e, Iterator))

print(isinstance(a, Iterable), isinstance(b, Iterable), isinstance(c, Iterable), isinstance(d, Iterable), isinstance(e, Iterable))

print(isinstance(a, Iterator) and isinstance(a, Iterable))

# 迭代器
# 可以直接作用于for 循环的对象统称为可迭代对象：Iterable
# 可以被next() 函数调用并不断返
