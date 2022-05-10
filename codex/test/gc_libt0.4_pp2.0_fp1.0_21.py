import gc, weakref

class A(object):
    pass

a = A()
b = A()

def callback(r):
    print("Callback called with", r)

r = weakref.ref(a, callback)

print("a:", a)
print("b:", b)
print("r:", r)
print("r():", r())

del a
gc.collect()

