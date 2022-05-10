import weakref
# Test weakref.ref()
from test.support import verbose, run_unittest
class C(object):
    pass
ob = C()
wr = weakref.ref(ob)
if verbose:
    print(wr)
    print(wr())
    print(wr is ob)
    print(wr() is ob)
# Make sure wr() is ob
assert wr() is ob
# Make sure wr() is still ob
assert wr() is ob
# Make sure wr() raises TypeError on garbage-collected ob
del ob
import gc
gc.collect()
try:
    wr()
except TypeError:
    pass
else:
    print('TypeError not raised')
    # Make sure wr() raises TypeError
    try:
        wr()
    except TypeError:
        pass
    else:
        print('TypeError not raised')
# Test weakref.proxy()
from test.support import verbose
class C(object):
    pass
ob = C()
p = weakref.proxy(ob)
if verbose:
    print(p)
    print(p is ob)
