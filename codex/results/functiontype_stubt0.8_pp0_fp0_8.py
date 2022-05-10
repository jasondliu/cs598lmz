from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
print(type(a), type(b), isinstance(a, list), isinstance(b, list))
# <class 'generator'> <class 'list'> False True
c = {x for x in [1]}
print(type(c), isinstance(c, set))
# <class 'set'> True
d = {x: x for x in [1]}
print(type(d), isinstance(d, dict))
# <class 'dict'> True
e = set()
print(type(e), isinstance(e, set))
# <class 'set'> True
f = list()
print(type(f), isinstance(f, list))
# <class 'list'> True

# 使用isinstance()判断一个对象是否是函数
from types import FunctionType


def fn():
    pass


a = FunctionType(fn.__code__, fn.__globals__, name=fn.__name__,
                 argdefs=fn.__
