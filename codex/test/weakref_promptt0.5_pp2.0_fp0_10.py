import weakref
# Test weakref.ref
import pickle

class C:
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

print(r(), p)
print(r() is p)
print(o is p)
print(o is r())

o2 = pickle.loads(pickle.dumps(o))
print(o2 is o)

r2 = pickle.loads(pickle.dumps(r))
print(r2(), r2() is o)

p2 = pickle.loads(pickle.dumps(p))
print(p2, p2 is o)
