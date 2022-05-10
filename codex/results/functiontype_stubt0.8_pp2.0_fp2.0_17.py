from types import FunctionType
a = (x for x in [1])
b = (x for x in [1, 2])
import datetime
c = datetime.timedelta(days=8)
d = datetime.timedelta(days=8)
for x in (a, b, c, d):
    print(type(x))
    print(FunctionType in map(type, gc.get_referrers(x)))

print()

from types import FrameType
from functools import partial
a = FrameType(partial(None))
b = FrameType(partial(None, 1))
c = FrameType(partial(None, x=1))
for x in a, b, c:
    print(type(x))
    print(FrameType in map(type, gc.get_referrers(x)))

print()

from types import MethodType
a = MethodType(partial(None), 1)
b = MethodType(partial(None), 1, 1)
c = MethodType(partial(None), 1, x=1)
for x in a, b, c:
    print(type(x))
   
