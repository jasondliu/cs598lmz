import gc, weakref
import copy
from functools import partial
import re

def _get_trace_back():
    import traceback
    return traceback.extract_stack()[:-1]

def _get_trace_back_str():
    import traceback
    return '\n'.join(traceback.format_list(_get_trace_back()))

def _get_caller_info():
    import inspect
    return inspect.stack()[2]

def _get_caller_info_str():
    import inspect
    return str(inspect.stack()[2])

def _get_local_vars_str(frame):
    import inspect
    return str(inspect.getargvalues(frame))

def _get_obj_id(obj):
    return id(obj)

def _get_obj_repr(obj):
    return repr(obj)

def _get_obj_type(obj):
    return type(obj)

def _get_obj_name(obj):
    return obj.__name__

def _get_
