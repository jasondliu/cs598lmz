import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc

gc.collect()
# ========================================================================
# See test_descr.py for more tests.
# ========================================================================

# Test larger than sys.getrecursionlimit stack
# Create a script that calls itself recursively to some large depth
script = """
import sys
def recurse(level, limit):
    if level < limit:
        return level + recurse(level+1, limit)
    return 0
def test_main():
    return recurse(0, %s)
def target(*args):
    return test_main()
"""

# One-off test (not in a loop) to check it doesn't hit the recursion limit
def test_recursive_call_large_stack():
    from test.script_helper import assert_python_ok

    # Ensure that calling the script with a large recursion limit succeeds
    assert_python_ok('-c', script % sys.getrecursionlimit() + "; target()")

    # Ensure that calling the script with a recursion limit of one less than
    # the script's recursion fails with a recursion error.
