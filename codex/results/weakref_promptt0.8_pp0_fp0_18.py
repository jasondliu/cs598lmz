import weakref
# Test weakref.ref()
import random

class C:
    pass

o = C()
r = weakref.ref(o)

# Accessing o directly is OK
print o

# Accessing o through the ref is OK
print r()

# Accessing o after deleting it directly is an error
del o
try:
    print o
except NameError as e:
    print e

# Accessing o through the ref returns None
print r()

# The ref no longer points to o after o is deleted
r = None
print o

# Creating a new object with the same id() as o
# will not affect the weakref to o
o = C()
print o
print r()

# As long as a ref is alive, the object is kept alive
o = C()
r = weakref.ref(o)
del o
print r()
o = C()
print r()

# Weak value dictionary
d = weakref.WeakValueDictionary()
o1 = C()
o2 = C()
o3 = C()
d['A'] = o1
d['B
