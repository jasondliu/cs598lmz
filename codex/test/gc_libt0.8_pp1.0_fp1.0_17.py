import gc, weakref, shlex
from functools import partial, wraps
from contextlib import contextmanager
from itertools import cycle

from numpy import asarray
from numpy.random import random_integers, random

