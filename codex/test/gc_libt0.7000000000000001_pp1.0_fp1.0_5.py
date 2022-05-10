import gc, weakref
from weakref import WeakKeyDictionary
from functools import reduce, partial
from collections.abc import Mapping
from inspect import signature, _empty
from types import FunctionType, MethodType, BuiltinFunctionType
from operator import attrgetter, itemgetter
from itertools import islice, chain, zip_longest, starmap

