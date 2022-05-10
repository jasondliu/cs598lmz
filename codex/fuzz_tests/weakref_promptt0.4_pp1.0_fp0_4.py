import weakref
# Test weakref.ref()

class C:
    pass

o = C()
w = weakref.ref(o)

print(w)
print(w())

del o
print(w)
print(w())

# Test weakref.WeakKeyDictionary()

class C:
    pass

o = C()
w = weakref.WeakKeyDictionary()
w[o] = 1

print(w)
print(w[o])

del o
print(w)

# Test weakref.WeakValueDictionary()

class C:
    pass

o = C()
w = weakref.WeakValueDictionary()
w[1] = o

print(w)
print(w[1])

del o
print(w)
