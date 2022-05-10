import weakref
# Test weakref.ref
r = weakref.ref(1)
r()

def f():
    return 1
# Test weakref.ref(function)
r = weakref.ref(f)
r()

import sys
if sys.version_info[0] == 2:
    class P(object): pass
else:
    class P: pass

p = P()
p = P()
# Test weakref.ref(instance)
r = weakref.ref(p)
r()

# Test weakref.proxy
r = weakref.proxy(p)
r
r.__class__
r.__doc__
r.__getattribute__
r.__setattr__
r.__repr__
r.__hash__
r.__nonzero__
r.__unicode__
r.__format__
r.__cmp__
r.__lt__
r.__le__
r.__gt__
r.__ge__
r.__init__
r.__new__
r.__reduce_ex__
r.__reduce__
r.__sub
