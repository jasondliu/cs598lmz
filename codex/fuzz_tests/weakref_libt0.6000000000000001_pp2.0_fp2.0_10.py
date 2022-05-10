import weakref
import re
import sys
import traceback
import random
import itertools
import bisect
import uuid
from collections import deque, namedtuple
from heapq import heappush, heappop
from operator import itemgetter
from functools import partial
from contextlib import contextmanager
from datetime import datetime, timedelta
from threading import Thread, Lock


class _LazyLoad(object):
    def __init__(self, loader):
        self.loader = loader
        self.value = None

    def __repr__(self):
        if self.value is None:
            self.value = self.loader()
        return repr(self.value)

    def __str__(self):
        if self.value is None:
            self.value = self.loader()
        return str(self.value)

    def __int__(self):
        if self.value is None:
            self.value = self.loader()
        return int(self.value)

    def __float__(self):
        if self.value is None:
            self
