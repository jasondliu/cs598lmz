import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

def callback(ignored):
    print('called back')

class A:
    def __init__(self):
        self.callback = callback
        self.wr = weakref.ref(self, self.callback)

a = A()
a = None
gc.collect()

# Test gc.garbage

class B:
    def __init__(self):
        self.wr = weakref.ref(self, self.callback)
    def callback(self, ignored):
        print('called back')

b = B()
b.wr()
b = None
gc.collect()
print(gc.garbage)

# Test gc.get_referrers

class C:
    def __init__(self):
        self.wr = weakref.ref(self, self.callback)
    def callback(self, ignored):
        print('called back')

c = C()
c.wr()
c = None
gc.collect()
print(gc.get_referrers(gc.garbage[0]))

# Test
