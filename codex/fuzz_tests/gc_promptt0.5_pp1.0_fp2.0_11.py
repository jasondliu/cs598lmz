import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

def make_cycle():
    o = C()
    o.x = o

def make_cycle_with_finalizer():
    class F:
        def __del__(self):
            pass
    o = F()
    o.x = o

print 'collecting...'
gc.collect()
print 'done'

print 'making cycles...'
for i in range(10):
    make_cycle()
    make_cycle_with_finalizer()
print 'done'

print 'collecting...'
gc.collect()
print 'done'

l = []
print 'creating l...'
for i in range(10):
    l.append(C())
print 'done'

print 'collecting...'
gc.collect()
print 'done'

print 'deleting l...'
del l
print 'done'

print 'collecting...'
gc.collect()
print 'done'

print 'creating l...'
l = [C() for i in range(10)]
