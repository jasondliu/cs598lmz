import weakref
# Test weakref.ref functionality

import weakref
import unittest
import sys
import gc
import operator
import random
import io


def pick_an_attribute(obj):
    # Helper to pick a random attribute from an object.
    # This is needed to handle the fact that int objects have a variable
    # number of attributes, depending on the platform.
    # Return None if obj has no attributes.
    attr = None
    names = dir(obj)
    if names:
        attr = random.choice(names)
    return attr

def count_allocations(func, *args):
    # Count the number of allocations required to run func(*args).
    gc.collect()
    before = gc.get_count()
    func(*args)
    gc.collect()
    return gc.get_count() - before

class Foo:
    def __del__(self):
        pass


class TestWeakref(unittest.TestCase):

    def test_ref(self):
        before = count_allocations(weakref.ref, Foo)
       
