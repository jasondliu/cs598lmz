import gc, weakref
import os, sys
import tempfile, shutil
import atexit
import cPickle as pickle
import numpy as np

try:
    from . import _np_utils
except ImportError:
    from ._np_utils import ArrayBox
else:
    from ._np_utils import ArrayBox as _ArrayBox

__all__ = ['StreamFileObject', 'StreamArray', 'BigArray']

# From Python's Lib/tempfile.py
template = 'tempfile-%d-%d-%d'
names = []

def _set_name():
    dir = tempfile.gettempdir()
    while True:
        name = os.path.join(dir, template % tuple(os.getpid() for i in range(3)))
        if not os.path.exists(name):
            return name

class _StreamNode(object):
    """_StreamNode(file_name=None, size=None, offset=None, parent=None,
                   dtype=None, readonly=False)

    An internal class to represent a node (slice) of a
