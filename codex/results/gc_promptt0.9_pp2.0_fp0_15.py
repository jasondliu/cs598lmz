import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(2) --------------------------------------------------
print('---Use "gc.collect(2)"---')
import gc, weakref
class A():
    def __del__(self):
        print('A __del__ called')

class B():
    def __del__(self):
        print('B __del__ called')


class C(B):
    def __del__(self):
        print('C __del__ called')


def f():
    a = A()
    r1 = weakref.ref(a)
    r2 = weakref.ref(a)
    b = C()
    r3 = weakref.ref(b)

f()
gc.collect(2)
"""
@endcode

- __Use gc.get_referrers()__: We can use gc.get_referrers() to see that there is a reference 
in gc.garbage.

@code
print(gc.get_referrers(r1))
#return: [{'r1': <weakref at 0x101088568; to '
