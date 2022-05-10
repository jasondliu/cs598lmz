import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))

a = A()
print('a: {0}'.format(hex(id(a))))
print('a.b: {0}'.format(hex(id(a.b))))
print('a.b.a: {0}'.format(hex(id(a.b.a))))
print('a.b.a.b: {0}'.format(hex(id(a.b.a.b))))

# Test gc.collect()
gc.collect()

# Test gc.get_referrers()
print('gc.get_referrers(
