from types import FunctionType
a = (x for x in [1])
a

def a():
    return 1

type(a)

def a(*args, **kwargs):
    pass

import random
isinstance(random.choice, FunctionType)

import _operator
isinstance(a, _operator.itemgetter)

isinstance(random.choice, _operator.itemgetter)

isinstance(a, FunctionType)

dir(_operator)
import functools
isinstance(a(), functools.partial)

isinstance(a(), _operator.attrgetter)

isinstance(a, functools.partial)

a

functools.partial

operator.itemgetter(0)([1, 2])

functools.partial(max, [1,2])

import inspect
inspect.signature
inspect.signature(functools.partial(max, [1,2]))

def a(b, *args, c=(), d=0, **kwargs):
    pass

inspect.signature(a)
a

inspect.signature(
