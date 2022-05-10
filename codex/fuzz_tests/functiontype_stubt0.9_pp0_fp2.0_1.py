from types import FunctionType
a = (x for x in [1])
isinstance(a, Iterator)

b = FunctionType(lambda: None)
type(b)

c = [x for x in [1]]
type(c)

d = map(lambda x: x, [1])
type(d)

e = list(range(1))
type(e)
import functools
a = functools.reduce(lambda x, y: x*y, [1, 2, 3])
print(a)

b = [x*y for x, y in zip([1, 2, 3], [2, 3, 4])]
print(b)

c = (x*y for x, y in zip([1, 2, 3], [2, 4, 4]))
d = 0
for num in c:
    d += num
print(d)

e = [x*y for x, y in zip(range(1, 10), range(1, 10))]
print(e)

f = functools.reduce(lambda x, y: x+y, [x*y for x,
