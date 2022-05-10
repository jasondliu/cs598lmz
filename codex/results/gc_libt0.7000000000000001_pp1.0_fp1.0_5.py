import gc, weakref
from weakref import WeakKeyDictionary
from functools import reduce, partial
from collections.abc import Mapping
from inspect import signature, _empty
from types import FunctionType, MethodType, BuiltinFunctionType
from operator import attrgetter, itemgetter
from itertools import islice, chain, zip_longest, starmap

from .functions import (neg, add, sub, mul, div, floordiv, mod, pow, lshift,
                        rshift, and_, or_, xor, eq, ne, lt, gt, le, ge)
from .functions import getitem, getattr, getitem_, getattr_
from .functions import setitem, setattr, setitem_, setattr_
from .functions import delitem, delattr, delitem_, delattr_
from .functions import pos, abs, invert, len_, contains, not_, truth
from .functions import concat, contains_, iadd, isub, imul, itruediv, ifloordiv
from .functions import imod, ip
