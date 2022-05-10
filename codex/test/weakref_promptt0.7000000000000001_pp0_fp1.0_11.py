import weakref
# Test weakref.ref(array)
import numpy as np
import gc
import sys

def test_weakref_array():
    x = np.arange(10)
    y = x
    z = weakref.ref(y)
    assert z() is y
    x = None
    y = None
    gc.collect()
    assert z() is None


def test_weakref_array_base():
    x = np.arange(10)
    y = x
    z = weakref.ref(x)
    assert z() is x
    x = None
    y = None
    gc.collect()
    assert z() is None

def test_weakref_array_base_memory_leak():
    """
    Regression test for memory leak.
    See issue #2166
    """
    def create_ref(x):
        return weakref.ref(x)

    N = 100
    M = 100

    # create a large object with a reference cycle
    x = np.zeros((N,N))
