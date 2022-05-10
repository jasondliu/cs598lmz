import weakref
# Test weakref.ref() with a bound method
class A:
    def meth(self):
        pass
a = A()
a_ref = weakref.ref(a.meth)
a.meth = None
print(a_ref())
del a
print(a_ref())

# Specify an anonymous callback for weak reference
def callback(ref):
    print("object dead")
    print(ref)
a = A()
a_ref = weakref.ref(a, callback)
a.meth = None
print(a_ref())
del a


# Test weakref.proxy() with a bound method
a = A()
p = weakref.proxy(a)
print(p.meth())
del a
try:
    print(p.meth())
except ReferenceError:
    print("ReferenceError")
p.meth = None
try:
    del p.meth
except ReferenceError:
    print("ReferenceError")
try:
    print(p.meth())
except ReferenceError:
    print("ReferenceError")
try:
    del p.meth
