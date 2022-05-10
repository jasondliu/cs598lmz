fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del fn, gi

def b():
    return a()
def a():
    return b()
def applyD(fn):
    return fn()
import sys
try:
    result = applyD(a)
except RuntimeError as e:
    print(e.__class__.__name__, sys.exc_info()[-1])
    result = "ERROR"
print(result)

"""
Expected: maximum recursion depth exceeded
"""

# The version of this in the spec is flawed.  It should be the same as
# test 3, just with arg() returning the function object instead of the
# result of calling it.

"""
$ python3 stack_infinite_recursion_1.py
RuntimeError RuntimeError('maximum recursion depth exceeded',)
ERROR
"""
