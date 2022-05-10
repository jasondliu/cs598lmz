import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

import sys, gc
class A:
    pass

for i in range(4):
    a = A()
    a.foo = i
    a.bar = 'a'
    a.spam = A()
    a.spam.cake = 'yummy!'

gc.collect()

# Test isinstance()

print(isinstance([], list))
print(isinstance((), tuple))
print(isinstance(sys, object))

# Test issubclass()

class B(A):
    pass

print(issubclass(B, A))
print(issubclass(A, B))

# Test locals()

def g(a, b=1, *args, **kwargs):
    print(a, b, args, kwargs)

g(3)
print(locals())

# Test map()

class M(object):
    def __init__(self, *args):
        self.args = args
    def __hash__(self):
        h = 0
        for arg in self.args
