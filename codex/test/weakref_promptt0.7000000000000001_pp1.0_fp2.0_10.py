import weakref
# Test weakref.ref support for objects
class C:
    pass
o = C()
r = weakref.ref(o)
print(r())
print(r() is o)
o2 = C()
r2 = weakref.ref(o2)
print(r2() is o2)
print(r2() is o)

import weakref
# Test weakref.ref support for old-style classes
class C:
    pass
o = C()
r = weakref.ref(o)
print(r())
print(r() is o)
o2 = C()
r2 = weakref.ref(o2)
print(r2() is o2)
print(r2() is o)

import weakref
# Test weakref.ref(x, f)
class C:
    def __del__(self):
        print('del')
o = C()
r = weakref.ref(o, lambda x: print('callback', x))
del o
print('end of test')

import weakref
# Test weakref.ref(x, f)
