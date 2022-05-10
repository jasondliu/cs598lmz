import weakref
# Test weakref.ref(subtype)
import pickle

class X(list):
    pass

class Y(X):
    pass

x = X()
x.a = 1
x.b = 2
x.c = 3

r = weakref.ref(x)

print(r().a)
print(r().b)
print(r().c)

s = pickle.dumps(r)
r2 = pickle.loads(s)

print(r2().a)
print(r2().b)
print(r2().c)

print('weakref.ref(subtype)')
y = Y()
y.a = 1
y.b = 2
y.c = 3

r = weakref.ref(y)
print(r().a)
print(r().b)
print(r().c)

s = pickle.dumps(r)
r2 = pickle.loads(s)

print(r2().a)
print(r2().b)
print(r2().c)
