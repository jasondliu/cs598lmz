import weakref
# Test weakref.ref() on a function.
import pickle

def f(): pass
r = weakref.ref(f)
print r() is f
print pickle.loads(pickle.dumps(r))() is f

# Test weakref.ref() on a class.
class C: pass
r = weakref.ref(C)
print r() is C
print pickle.loads(pickle.dumps(r))() is C

# Test weakref.ref() on an instance.
x = C()
r = weakref.ref(x)
print r() is x
print pickle.loads(pickle.dumps(r))() is x
