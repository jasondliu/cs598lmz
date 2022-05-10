import gc, weakref
from collections import OrderedDict
from functools import partial
from itertools import chain
from operator import attrgetter
from types import MethodType, FunctionType
from unittest import TestCase

