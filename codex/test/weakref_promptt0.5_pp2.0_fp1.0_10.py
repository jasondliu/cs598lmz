import weakref
# Test weakref.ref()'s ability to handle objects that have a __del__ method.
import gc
import sys
from test import support
from test.support import gc_collect
from test.support.script_helper import assert_python_ok

# Create a bunch of objects that have a __del__ method.
class C:
    def __del__(self):
        pass

objects = [C() for i in range(100)]

# Create a bunch of references to those objects.
refs = [weakref.ref(obj) for obj in objects]

# Clear the references to the objects.
objects = None

# Collect the unreferenced objects.
gc_collect()

# Check that the objects have been collected.
for r in refs:
    assert r() is None

# Check that the objects' __del__ methods have been called.
for r in refs:
    assert r.__del__.called

# Create a bunch of objects that have a __del__ method.
class C(object):
    def __del__(self):
        pass

