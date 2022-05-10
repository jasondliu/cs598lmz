from types import FunctionType
a = (x for x in [1])
isinstance(a, FunctionType)

a.__class__.__mro__

a.__class__.__name__

b = (x for x in [1])

import inspect
inspect.isgenerator(a)

inspect.isgenerator(b)

inspect.gencell(b)

inspect.isgeneratorfunction(a.__iter__)

inspect.isgeneratorfunction(b.__iter__)

def gen():
    yield 1

for value in gen():
    print('Hello {0}'.format(value))
