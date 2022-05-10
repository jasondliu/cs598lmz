import weakref
# Test weakref.ref() and weakref.proxy()

class MyClass:
    def __init__(self):
        print "Initializing..."
        self.a = 1
        self.b = 2

inst = MyClass()

ref = weakref.ref(inst)
print "ref() =", ref()
print "dir(ref()) =", dir(ref())
print "ref().b =", ref().b
print "weakref.proxy(inst).b =", weakref.proxy(inst).b
print "dir(weakref.proxy(inst)) =", dir(weakref.proxy(inst))

try:
    print "ref().a =", ref().a
except Exception, x:
    print x

try:
    print "ref().c =", ref().c
except Exception, x:
    print x

try:
    print "weakref.proxy(inst).a =", weakref.proxy(inst).a
except Exception, x:
    print x

try:
    print "weakref.proxy(inst).c =", weakref.proxy(inst).c
except Exception
