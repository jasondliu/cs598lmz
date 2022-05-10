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

x = D()

print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())

del x

print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())

# Test weakrefs

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

x = D()

def callback(reference):
    print("callback")

x_ref = weakref.ref(x, callback)
print(x_ref)

del x

print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())

print(x_ref)

print(gc.collect())
print(gc.collect())
print
