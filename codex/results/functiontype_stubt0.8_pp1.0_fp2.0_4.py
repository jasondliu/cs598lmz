from types import FunctionType
a = (x for x in [1])

b = [1, 2, 3, 4]

c = {'a': 1, 'b': 2}

d = {'a': 1, 'b': 2}.values()

e = [1, 2, 3, 4][:]

f = {'a': 1, 'b': 2}.copy()

g = FunctionType(lambda x:x, globals=globals())

del a
del b
del c
del d
del e
del f
del g

import gc
print(gc.get_objects())
