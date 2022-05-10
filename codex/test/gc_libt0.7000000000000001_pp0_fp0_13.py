import gc, weakref

class A:
    pass

gc.disable()
a = A()
# a.b = a
# a.c = [a, 2]
a.d = {'a': a, 'b': 2}
a.e = weakref.ref(a)

print(gc.get_referents(a))
print(type(gc.get_referents(a)[0]))
del a
gc.collect()
print(gc.garbage)
