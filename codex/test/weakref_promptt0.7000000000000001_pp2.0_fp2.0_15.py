import weakref
# Test weakref.ref for a class instance.
class C:
    pass
instances = []
for i in range(10):
    c = C()
    r = weakref.ref(c)
    instances.append((c, r))
del c
print(instances)

# Test weakref.ref for an old-style class instance.
class C:
    pass
instances = []
for i in range(10):
    c = C()
    r = weakref.ref(c)
    instances.append((c, r))
del c
print(instances)

# Test weakref.ref for an instance of a builtin type.
instances = []
for i in range(10):
    c = i
    r = weakref.ref(c)
    instances.append((c, r))
del c
print(instances)
