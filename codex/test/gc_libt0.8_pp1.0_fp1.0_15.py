import gc, weakref
from functools import partial
from threading import Lock,RLock
from inspect import getargspec
from itertools import chain
from collections import defaultdict
from types import MethodType
from time import time, sleep
