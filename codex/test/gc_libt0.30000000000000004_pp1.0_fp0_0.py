import gc, weakref

class C:
    def __init__(self):
        self.a = 1
        self.b = 2

def f():
    c = C()
    print(c.a)
    print(c.b)
    return c

c = f()
print(c.a)
print(c.b)

print("\n")

wref = weakref.ref(c)
print(wref)
print(wref())

print("\n")

del c
gc.collect()
print(wref)
print(wref())

print("\n")

print(wref() is None)
