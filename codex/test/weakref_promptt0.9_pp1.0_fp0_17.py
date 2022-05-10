import weakref
# Test weakref.ref(proxy(o))
class A:
    a = 1

class B:
    b = 2

class Points(list):
    def __init__(self, x):
        self[:] = x
    def __str__(self):
        return 'points(' + ', '.join(map(str, self)) + ')'

a = A()
a.x = Points([(0.0, 0.0), (1.0, 1.0)])
b = B()
b.x = Points([(2.0, 2.0), (3.0, 3.0)])

a_ref = weakref.ref(a)
a_ref_x = weakref.ref(a.x)
b_ref = weakref.ref(b)
b_ref_x = weakref.ref(b.x)

a_proxy = weakref.proxy(a)
a_proxy_x = weakref.proxy(a.x)
b_proxy = weakref.proxy(b)
b_proxy_x = weakref.proxy(b.x)
