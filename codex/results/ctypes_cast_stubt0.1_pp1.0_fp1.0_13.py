import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import os
import sys
import time
import logging
import threading
import traceback
import warnings
import weakref

# SOURCE LINE 13

import gevent
from gevent import core
from gevent.hub import get_hub, getcurrent, PYPY
from gevent.timeout import Timeout
from gevent.event import Event
from gevent.greenlet import Greenlet
from gevent.util import wrap_errors, copy_globals

# SOURCE LINE 21

__all__ = ['Greenlet',
           'GreenletExit',
           'spawn',
           'spawn_later',
           'spawn_raw',
           'spawn_raw_later',
           'spawn_link',
           'spawn_link_value',
           'spawn_link_exception',
           'spawn_link_exception_type',
           'spawn_n',
           'spawn_n_later',
           'spawn_link_n',
           'spawn_link_n_value',
           'spawn_link_
