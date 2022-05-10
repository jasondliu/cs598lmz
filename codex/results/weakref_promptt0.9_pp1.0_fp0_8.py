import weakref
# Test weakref.ref() when the object is deleted before the end of the
# weakref.ref() call.
class Boo:
    pass

def f(ref):
    print ref()

b = Boo()

ref = weakref.ref(Boo())
del Boo
ref()
try:
    f(weakref.ref(Boo()))
except ReferenceError:
    pass

del Boo
ref()

# Test that weakref survives class deletion
class X:
    pass

x = X()
r = weakref.ref(x)

del X
del x
try:
    print r()
except NameError:
    pass

# Test that weakref survives class deletion across files.
import weakref_classdel_support

x = weakref_classdel_support.X()
weakref_classdel_support.r = weakref.ref(x)

import sys
del sys.modules['weakref_classdel_support']
del x
try:
    print weakref_classdel_support.r()
except NameError:
    pass

# Test that weakref survives
