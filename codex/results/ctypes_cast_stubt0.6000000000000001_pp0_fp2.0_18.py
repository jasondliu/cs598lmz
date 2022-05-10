import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 10

import sys

def _mimport(name, level=1):
    try:
        return __import__(name, globals(), level=level)
    except:
        return __import__(name, globals())

import MDSplus
_mimport('_treeshr')

import numpy as _N
import numpy.ma as _Nm

def _getNid(obj):
    try:
        return obj.nid
    except:
        return obj

def _getNidList(obj):
    try:
        return [nid.nid for nid in obj]
    except:
        return obj

def _tdiCompile(expr):
    return _treeshr.tdiCompile(expr, _treeshr._C.Tree.currTree)

def _tdiEvaluate(expr):
    return _tdiCompile(expr).evaluate()

def _tdiExecute(expr):
    return _treeshr.tdi
