from types import FunctionType
a = (x for x in [1])
isinstance(a, GeneratorType)
True

# 判断某个对象是否是另一个类的子类
class A():
    pass
class B(A):
    pass
isinstance(B(), A)
True
issubclass(B, A)
True

# 判断两个索引类型的值是否相等
v = [10, 20, 30]
w = [10, 20, 40]
v == w
False
cmp(v, w)
-1
s = set([1, 2, 3])
t = set([1, 2, 3, 4, 5])
s == t
False
cmp(s, t)
-1
s.issubset(t)
True
cmp(frozenset(s), frozenset(t))
-1

# 判断一个对象是否是可调用的

