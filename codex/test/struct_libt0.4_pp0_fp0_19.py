import _struct
import _thread
import _threading
import _time
import _traceback
import _warnings
import _weakref

# This is a hack to prevent an import loop.
_sys = sys

import _weakrefset

# some helpers for simple types

def _make_cell_setter(name):
    def setter(self, value):
        self.__dict__[name] = value
    return setter

def _make_cell_getter(name):
    def getter(self):
        return self.__dict__[name]
    return getter

def _make_cell():
    return _make_cell_getter, _make_cell_setter

def _make_empty_cell():
    def getter(self):
        raise ValueError("empty cell")
    def setter(self, value):
        raise ValueError("empty cell")
    return getter, setter

# the public interface

from _collections import deque, defaultdict, OrderedDict

from _functools import partial, reduce

