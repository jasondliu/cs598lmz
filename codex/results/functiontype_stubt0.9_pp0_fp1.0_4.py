from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = (x for x in [1])
FunctionType.__mul__(a, b)

# Complex Types
# collections
# deque
import collections
d = collections.deque('xyz')
# d.appendleft('abc')
# print(d)
# d.extend('123')
# print(d)
d.extendleft('000')
print(d)
d.rotate(-2)
print(d)
# defaultdict

# namedtuple

# OrderedDict

# Counter

# heapq

# bisect

# itertools
# chain, chain.from_iterable
for c in itertools.chain([1, 2, 3], {4:5}, (4, 5, 1, 8)): print(c)
for c in itertools.chain.from_iterable([[1, 2, 3], [2, 3, 4]]): print(c)

# cycle
i = 0
for c in itertools.cycle(['a',
