import gc, weakref
from collections import defaultdict
from contextlib import contextmanager
from functools import partial
from itertools import chain
from operator import itemgetter
from weakref import WeakKeyDictionary

