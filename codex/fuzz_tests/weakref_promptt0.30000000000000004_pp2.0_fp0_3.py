import weakref
# Test weakref.ref(object)

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o = None

print(r)
print(r())

# Test weakref.ref(object, callback)

class C:
    pass

o = C()

def callback(r):
    print("callback called with", r)

r = weakref.ref(o, callback)

print(r)
print(r())

o = None

print(r)
print(r())

# Test weakref.proxy(object)

class C:
    pass

o = C()
r = weakref.proxy(o)

print(r)
print(r.__class__)

o = None

print(r)
print(r.__class__)

# Test weakref.proxy(object, callback)

class C:
    pass

o = C()

def callback(r):
    print("callback called with", r)

r
