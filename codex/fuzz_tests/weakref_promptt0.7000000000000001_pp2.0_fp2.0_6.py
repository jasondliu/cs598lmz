import weakref
# Test weakref.ref
import weakref

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def func1(inst):
    print "func1 is called on", inst and inst.name

def func2(inst):
    print "func2 is called on", inst and inst.name

def func3(inst):
    print "func3 is called on", inst and inst.name

a = Foo("a")
b = Foo("b")
c = Foo("c")

# testing a weakref on an object
print "Testing a weakref on an object"
w = weakref.ref(a, func1)
print "a is", a
print "weak reference to a is", w
print "deleting a"
del a
print

# testing a weakref on a dict key
print "Testing a weakref on a dict key"
d = {a:1, b:2, c:3}
print "d is", d

