import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)
import time
import os
import sys
import random
import string
import traceback
import common
import testlib
import types

# import weakref

# import pdb

# class WeakKeyDictionary(dict):
#     def __init__(self, *args, **kw):
#         super(WeakKeyDictionary, self).__init__(*args, **kw)
#         self.__weakref__ = weakref.ref(self)

# class WeakMethod(object):
#     def __init__(self, m):
#         self._m = m
#         self._obj = m.im_self
#         self.__weakref__ = weakref.ref(self._obj)

#     def __call__(self, *args, **kwargs):
#         return self._m(self._obj, *args, **kwargs)


