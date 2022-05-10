import weakref
# Test weakref.ref(obj)
# Test weakref.ref(obj, callback)
# Test weakref.proxy(obj)
# Test weakref.getweakrefcount(obj)
# Test weakref.getweakrefs(obj)
# Test weakref.WeakKeyDictionary()
# Test weakref.WeakValueDictionary()
# Test weakref.WeakSet()
# Test weakref.finalize(obj, callback)

import gc
import unittest
import operator
import sys
import os
import pickle
import test.support
import itertools
import collections
import contextlib
import weakref

# Test weakref.ref(obj)
# Test weakref.ref(obj, callback)
# Test weakref.proxy(obj)
# Test weakref.getweakrefcount(obj)
# Test weakref.getweakrefs(obj)
# Test weakref.WeakKeyDictionary()
# Test weakref.WeakValueDictionary()
# Test weakref.WeakSet()
# Test weakref.finalize(obj, callback)

class MyBase:
    pass

class My
