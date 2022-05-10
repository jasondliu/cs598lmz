import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hi'

fun.__dict__

@classmethod
def fun(cls, *args):
    return args

fun.__dict__

fun.__annotations__

from collections import namedtuple

Point = namedtuple('Point', 'x y')

p = Point(1, 2)
p.x
p.y

p.x = 42
p.x

t = p._asdict()
t['x']

print(t)

from collections import OrderedDict

o = OrderedDict()
o['foo'] = 1
o['bar'] = 2
o.keys()

d = {}
d['foo'] = 1
d['bar'] = 2
d.keys()

from operator import methodcaller

methodcaller('keys')()

o.keys()

from collections import deque

deque(o)

import dis
dis.dis(methodcaller('keys'))
