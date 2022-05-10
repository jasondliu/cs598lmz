import gc, weakref, sys
from contextlib import closing
from itertools import chain
from collections import OrderedDict
from functools import partial, wraps
from threading import Thread
