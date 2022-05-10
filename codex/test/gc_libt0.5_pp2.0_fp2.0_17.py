import gc, weakref
from collections import defaultdict
from functools import partial
from itertools import chain
from operator import itemgetter
from types import MethodType

from six import add_metaclass, itervalues

