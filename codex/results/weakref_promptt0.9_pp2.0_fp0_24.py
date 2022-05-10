import weakref
# Test weakref.ref()
def f1(x):
   return 42 + x
a = "12345"
wr = weakref.ref(a)
b = wr()
print b
c = wr()
print c
d = wr()
print d

# Test weakref.WeakReference()
class Foo(object):
   pass

def f2(x, y):
   return 42 + x + y

a = Foo()
wr = weakref.WeakReference(a)
b = wr()
print b

c = f2(b, 10)
print c

d = f2(b, 20)
print d
f = Foo()
wr = weakref.WeakKeyDictionary()
wr[f] = 1
print wr
g = wr[f]
print g

wr = weakref.WeakValueDictionary()
wr["123"] = f
print wr

g = wr["123"]
print g
f = weakref.WeakSet()
f.add(1)
f.add(2)
print f

f.add(1)
print f

a =
