import weakref
# Test weakref.ref() argument:
#
class C:
    pass

o = C()
r = weakref.ref(o)

print(r)

o2 = r()

print(o2 is o)

# Test weakref.ref(object, callback)
#
class D:
    pass

o = D()

def callback(reference):
    "callback function"
    print('callback(', reference, ')')

r = weakref.ref(o, callback)

print('deleting o')
del o

import gc
gc.collect()

# Test weakref.proxy()
#
class E:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return 'E(' + `self.value` + ')'

o = E(10)
p = weakref.proxy(o)

print(p.value)
print(p)

o = None

try:
    print(p.value)
except ReferenceError:
    print('ReferenceError
