import gc, weakref, sys

from collections import deque
from functools import partial
from threading import Condition, Lock, Thread, currentThread

