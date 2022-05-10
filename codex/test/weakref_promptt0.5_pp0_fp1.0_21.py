import weakref
# Test weakref.ref()

class A:
    pass

def f(x):
    print(x)

a = A()
a.x = 1
wr = weakref.ref(a, f)

print("wr is ", wr)
print("wr() is ", wr())
print("wr().x is ", wr().x)

del a
print("del a")

print("wr is ", wr)
print("wr() is ", wr())

# Test weakref.proxy()

class A:
    pass

a = A()
a.x = 1
wr = weakref.proxy(a)

print("wr is ", wr)
print("wr.x is ", wr.x)

del a
print("del a")

print("wr is ", wr)
print("wr.x is ", wr.x)

# Test weakref.getweakrefcount()

class A:
    pass

a = A()
a.x = 1
wr = weakref.ref(a)

print("wr is ", wr)
