import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref cycle.
print('gc.garbage initial:', gc.garbage)
gc.set_debug(gc.DEBUG_COLLECTABLE)
garbage = []
def callback(x):
    print('weak callback', x)
    if x not in garbage:
        garbage.append(x)
class A:
    def __del__(self):
        print('A.__del__')
    def __repr__(self):
        return 'A()'
a1 = A()
a2 = A()
w1 = weakref.ref(a1, callback)
w2 = weakref.ref(a2, callback)
a1.w1 = w1
a2.w2 = w2
a2.a1 = a1
a1.a2 = a2
w1()
w2()
print('a1:', a1)
print('a2:', a2)
del a1
del a2
print('garbage:', garbage)
gc.collect()
print('gc.garbage final:', gc.garbage
