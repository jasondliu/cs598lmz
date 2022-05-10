from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

print(type(a) == list)

# 方法二
from collections import Iterator
print(isinstance(a, Iterator))

# 方法三
from collections import Iterable
print(isinstance(a, Iterable))

# 方法四
print(hasattr(a, '__iter__'))

# 方法五
print(hasattr(a, '__next__'))
