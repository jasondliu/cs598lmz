import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

a = A()
b = B()
c = C()
d = D()

def show_refs(obj):
    print(obj, '->', [r for r in gc.get_referents(obj) if not isinstance(r, weakref.ReferenceType)])

print('a:')
show_refs(a)
print('b:')
show_refs(b)
print('c:')
show_refs(c)
print('d:')
show_refs(d)

print('collecting...')
n = gc.collect()
print('unreachable objects:', n)
print('a:')
show_refs(a)
print('b:')
show_refs(b)
print('c:')
show_refs(c)
print('d:')
show_refs(d)

print('a
