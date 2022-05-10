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

print("a:", a)
print("b:", b)
print("r:", r)
print("r():", r())

del b
gc.collect()

print("a:", a)
print("b:", b)
print("r:", r)
print("r():", r())

x = weakref.WeakKeyDictionary()
x[a] = 1
print(x)

del a
gc.collect()

print(x)

x = weakref.WeakValueDictionary()
x[1] = a
print(x)

del a
gc.collect()

print(x)

x = weakref.WeakSet
