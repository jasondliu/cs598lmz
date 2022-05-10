import weakref
# Test weakref.ref()

def f(x):
    print(x)

wref = weakref.ref(f)

print(wref)

wref()

wref = weakref.ref(f, lambda ref: print('dead'))

f = None

print('-' * 40)

# Test weakref.WeakValueDictionary

class A:
    pass

a = A()

a.x = 1

wdict = weakref.WeakValueDictionary()

wdict['a'] = a

print(wdict['a'].x)

del a

print(wdict)

# Test weakref.WeakKeyDictionary

class A:
    pass

a = A()

wdict = weakref.WeakKeyDictionary()

wdict[a] = 1

print(wdict[a])

del a

print(wdict)

# Test weakref.WeakSet

class A:
    pass

a = A()

wset = weakref.WeakSet()

wset.add
