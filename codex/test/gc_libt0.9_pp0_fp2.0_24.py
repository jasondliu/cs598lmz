import gc, weakref
from numbers import Number
from functools import reduce, partial
from operator import mul

from sys import intern
from types import BuiltinFunctionType, MethodType, BuiltinMethodType, FunctionType
from itertools import product
from weakref import ReferenceType
