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

