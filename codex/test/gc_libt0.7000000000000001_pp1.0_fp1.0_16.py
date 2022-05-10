import gc, weakref, inspect

class A:
    pass
gc.disable()

a = A()
a.x = a
del a  # create a reference cycle

p = weakref.WeakValueDictionary()

a = A()
a.x = a
p[id(a)] = a
print(a.x is a)
del a
print(gc.collect())
print(p)
print(p.data)
print(p.data.values())
