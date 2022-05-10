import weakref
# Test weakref.ref(array).
def print_ref(ref):
    print(ref())
a = [1, 2]
r = weakref.ref(a)
print('r',r)
r2 = weakref.ref(a)
print('r2',r2)
print_ref(r)
print_ref(r2)
del a
print_ref(r)
print_ref(r2)

a = [1, 2]
r = weakref.ref(a)
print_ref(r)
a.append(3)
print_ref(r)
del a[:]
print_ref(r)
a.append(4)
print_ref(r)
a = [1, 2]
print_ref(r)

# Test weakref.getweakrefcount
a = [1, 2]
print(weakref.getweakrefcount(a))
b = [3, a]
print(weakref.getweakrefcount(a))
c = [4, a]
print(weakref.getweakrefcount(a))

# Test weak
