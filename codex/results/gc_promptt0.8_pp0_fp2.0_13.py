import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with a collectable object.
class A:
    pass
a = A()
a_id = id(a)
a_ref = weakref.ref(a)
a = None
gc.collect()
print(gc.collect())
print(a_ref())
print(gc.collect())
print(a_ref())
##############################################################################
print('\n\n***** 1.2 *****')
from gc import get_count, collect
def report(enabled):
    print('\n%-16s %10s %10s' % ('', 'before', 'after'))
    fmt = '%-16s %10d %10d'
    # Always printed
    print('gc.get_count() =', end=' ')
    print(get_count())
    print('gc.isenabled() =', end=' ')
    print(isenabled())
    for i in range(4):
        if not enabled and i > 1:
            break
        collect()
        if i == 0:
            print(fmt % ('enabled=False,', *get_count()
