import weakref
# Test weakref.ref's cycle garbage collection.

class A:
    pass

a = A()
b = A()

# create a cycle
a.b = b
b.a = a


def callback(ref):
    print('callback(', ref, ')')


a_ref = weakref.ref(a, callback)
print('a_ref:', a_ref)
print('a_ref():', a_ref())

b_ref = weakref.ref(b, callback)
print('b_ref:', b_ref)
print('b_ref():', b_ref())


class C:
    pass

c = C()
d = C()

# create a cycle
c.d = d
d.c = c

c_ref = weakref.ref(c, callback)
print('c_ref:', c_ref)
print('c_ref():', c_ref())

d_ref = weakref.ref(d, callback)
print('d_ref:', d_ref)
print('d_ref():', d_ref())


