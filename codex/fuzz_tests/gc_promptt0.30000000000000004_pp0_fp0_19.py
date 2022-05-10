import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))

gc.collect()
a = A()
print('a: {0}'.format(hex(id(a))))
print('a.b: {0}'.format(hex(id(a.b))))
print('a.b.a: {0}'.format(hex(id(a.b.a))))

print('del a.b')
del a.b
print('del a')
del a
print('del B.a')
del B.a
print('gc.collect()')
gc.collect()

print('a: {0}'.format(hex(id(a))))
