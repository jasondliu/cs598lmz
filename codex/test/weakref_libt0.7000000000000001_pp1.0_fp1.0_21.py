import weakref
import inspect
import types
import itertools
import sys

from . import _compat, _util, _repr, _threading

def _is_event_handler(attr):
    for cls in (staticmethod, classmethod, property):
        if isinstance(attr, cls):
            attr = attr.__func__
    return inspect.isfunction(attr) and hasattr(attr, '_is_event_handler')

def _is_event_dependent(attr):
    for cls in (staticmethod, classmethod, property):
        if isinstance(attr, cls):
            attr = attr.__func__
    return inspect.isfunction(attr) and hasattr(attr, '_is_event_dependent')

def _is_event_observer(attr):
    for cls in (staticmethod, classmethod, property):
        if isinstance(attr, cls):
            attr = attr.__func__
    return inspect.isfunction(attr) and hasattr(attr, '_is_event_observer')

