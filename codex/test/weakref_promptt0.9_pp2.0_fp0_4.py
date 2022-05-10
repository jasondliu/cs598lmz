import weakref
# Test weakref.ref

# ref is a factory that returns a weak reference proxy to an object.
    
class Foo:
    pass

f = Foo()
x = weakref.ref(f)
print(x)
print(f is x())
#

# ref is a subclass of built-in function. So repr(x) returns a valid Python expression.


t = weakref.ref(f)

print(x is t)
print()


# This example shows how to create a callback function to detect when the referenced object has been deleted.

class Foo:
    pass
f = Foo()
r = weakref.ref(f)

def callback(r):
    print("The referenced object has been deleted")

r = weakref.weakref(f, callback)
print(r)
print(r())

print(f is r())
print()


# This example shows how to create weak references to a given class instance.

class Foo(object):
    def __init__(self, name):
        self.name = name
        
