import gc, weakref
from collections import defaultdict
from functools import wraps
from itertools import chain
from operator import attrgetter
from types import MethodType

