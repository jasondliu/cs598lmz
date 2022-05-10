import weakref
# Test weakref.ref for a particular instance.
import weakref

# Create a class with a method...

class MyClass:

    def myMethod(self):
        return id(self)

# ... and create an instance of that class

myObj = MyClass()

# Create a weak reference to the instance

my_weakref = weakref.ref(myObj)

# This should invoke the method bound to myObj

print id(myObj), my_weakref().myMethod()

print "*"*80
# A class for testing weak references.
# Imports.
import weakref

class Test(object):
    def __init__(self, name):
        self.name = name
        print('(Creating %s)' % self.name)
    def __del__(self):
        print('(Destroying %s)' % self.name)

# Create a test object and a weak reference proxy to it.
t = Test('test')
w = weakref.ref(t)
if w() is not None:
    print('t is still alive')
else:
   
