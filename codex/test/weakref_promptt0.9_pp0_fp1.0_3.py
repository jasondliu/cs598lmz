import weakref
# Test weakref.ref with C API

# This is a modified version of weakref_cobject.py.  The types tested
# aren't supported by all Python builds.

import test.test_support
import weakref
import UserDict

# the event callback is called with a list of all registered callbacks
# and a list of all dead callbacks
