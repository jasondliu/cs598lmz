import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C(object):
    pass

def func():
    pass

# Create a bunch of objects
for i in range(10):
    C()
    func()
    func
    [1, 2, 3, 4]
    {'a': 1, 'b': 2}
    'abc'

# Create a cycle
c1 = C()
c2 = C()
c1.foo = c2
c2.foo = c1
del c1, c2

# Create a bunch of weakrefs
for i in range(10):
    weakref.ref(C())
    weakref.ref(func)
    weakref.ref(func)
    weakref.ref([1, 2, 3, 4])
    weakref.ref({'a': 1, 'b': 2})
    weakref.ref('abc')

# Create some weakrefs with callbacks
def callback(arg):
    print arg
for o in [C(), func, func, [1, 2, 3, 4], {'a': 1, 'b': 2}, '
