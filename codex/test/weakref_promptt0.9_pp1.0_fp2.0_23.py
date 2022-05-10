import weakref
# Test weakref.ref() with callable objects that care about __func__.

import unittest
from test import support
from collections import UserString
from test.mapping_tests import MappingProtocolTest

from weakref import WeakValueDictionary
from weakref import WeakKeyDictionary
from weakref import ProxyTypes
from weakref import ReferenceType
from weakref import WeakSet
from weakref import WeakMethod
from weakref import finalize
from weakref import KeyedRef
from weakref import WeakMethodType

from functools import partial
from types import ClassType
from types import MethodType
from types import FunctionType

from sys import getrefcount

from contextlib import redirect_stdout
from types import BuiltinMethodType

from test import mapping_tests

# Disable this for this test module; the weak ref tests need to create
# cyclic trash.
support.check_impl_detail = lambda *args, **kwargs: None

# ===========================================================================
# Basic tests

class C(object):
    pass

class D(C):
    pass

class E:
    pass

