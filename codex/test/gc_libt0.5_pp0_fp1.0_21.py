import gc, weakref
from copy import copy
from types import FunctionType
from functools import partial
from itertools import chain
from collections import deque
from inspect import getargspec
from weakref import WeakKeyDictionary
from threading import Lock
from collections import namedtuple
from functools import wraps

