import gc, weakref, sys, time, inspect
from threading import Lock, Event
from copy import copy, deepcopy
from bisect import bisect, insort
from collections import Iterable, Iterator, Sequence
from itertools import islice, chain
from operator import attrgetter, itemgetter
from .funcs import mget, mitemgetter, where, assert_one, sign
from .iters import unique, unique_everseen, unique_justseen, allbutlast, itervalues
from .futures import *
from .anycall import *
from .misc import *
from .runtime import *
from .introspection import *

#: Create a fully qualified ``get()`` based on the given model and the specified
#: lookupable objects.
#: Lookupable objects can be:
#:
#: - a single :class:`str`
#: - a sequence of :class:`str`
#: - a :class:`dict` with :class:`str` keys
#: - a :class:`dict` with :class:`str` keys, and :class
