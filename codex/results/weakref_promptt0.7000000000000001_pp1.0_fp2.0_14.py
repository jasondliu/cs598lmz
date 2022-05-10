import weakref
# Test weakref.ref() and weakref.getweakrefcount()
import _weakref

base = []

try:
    baseref = weakref.ref(base)
except TypeError:
    pass
else:
    print('weakref.ref(base) should fail')

try:
    baseref = weakref.ref(base, lambda: None)
except TypeError:
    pass
else:
    print('weakref.ref(base, lambda: None) should fail')

class C:
    pass

c = C()
c.attr = []

try:
    cref = weakref.ref(c.attr)
except TypeError:
    pass
else:
    print('weakref.ref(c.attr) should fail')

try:
    cref = weakref.ref(c.attr, lambda: None)
except TypeError:
    pass
else:
    print('weakref.ref(c.attr, lambda: None) should fail')

def callback(ignore):
    print('callback called')

a = []
r = weakref.
