gi = (i for i in ())
# Test gi.gi_code is code with 0 arguments.
if gi.gi_code.co_argcount != 0:
    raise TestFailed, "closure been called too early (1)"

count = 0
def f(i):
    def g():
        nonlocal count
        count = count + 1
        if count > 1:
            raise TestFailed, "closure been called too early (2)"
    g()

del count
[f(i) for i in (1, 2, 3)]

for i in range(10):
    exec('def f(): pass')

def g():
    yield
    return 5

def f():
    return g()

x = f()
if x.__next__() != None:
    raise TestFailed, "__call__ return value from non-None gi_yieldfrom"
if x.__next__() != 5:
    raise TestFailed, "__call__ from non-None gi_yieldfrom"

import sys

# This class attempts to trick the compiler into thinking it defines
# xx__getitem__
class C
