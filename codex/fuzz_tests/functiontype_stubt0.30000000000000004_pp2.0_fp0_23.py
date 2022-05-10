from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {x: x for x in [1]}
e = FunctionType(lambda: None, {})
print(a, b, c, d, e)

# 判断对象是否可调用
print(callable(a), callable(b), callable(c), callable(d), callable(e))

# 判断对象是否可迭代
print(iter(a), iter(b), iter(c), iter(d), iter(e))

# 判断对象是否可迭代
print(isinstance(a, Iterable), isinstance(b, Iterable), isinstance(c, Iterable), isinstance(d, Iterable), isinstance(e, Iterable))

# 判断对象是否可迭代
print(isinstance(a, Iterator), isinstance(b
