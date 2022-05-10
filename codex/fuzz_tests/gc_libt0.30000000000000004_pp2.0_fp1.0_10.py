import gc, weakref
import os, sys
import time
import traceback
import types
import warnings

from . import _compat
from . import _util
from . import _weakref
from . import _weakrefset
from . import _threading
from . import _tracemalloc
from . import _tracemalloc_impl
from . import _tracemalloc_test
from . import _tracemalloc_test_impl
from . import _tracemalloc_test_weakref
from . import _tracemalloc_test_weakref_impl

# Python 2.x:
#   - weakref.ref(obj, callback) is not supported
#   - weakref.ReferenceType is not supported
#   - weakref.ProxyType is not supported
#   - weakref.getweakrefcount() is not supported
#   - weakref.getweakrefs() is not supported
#   - weakref.WeakKeyDictionary is not supported
#   - weakref.WeakValueDictionary is not supported
#   - weakref.finalize() is not supported
#   - weakref.Weak
