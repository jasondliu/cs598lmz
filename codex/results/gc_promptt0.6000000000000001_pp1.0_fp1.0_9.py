import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
    def __del__(self):
        print('deleting %d' % self.value)

def make_cycle():
    a = A(1)
    a.b = A(2)
    a.b.c = a

a = make_cycle()
print('Collecting')
n = gc.collect()
print('Unreachable objects:', n)
print('Remaining Garbage:', gc.garbage)

print(a)
print(a.b)
print(a.b.c)
print(a.b.c.b)
print(a.b.c.b.c)

print('Collecting again')
n = gc.collect()
print('Unreachable objects:', n)
print('Remaining Garbage:', gc.garbage)

# Test gc.get_referents()
a = A(1
