import types
types.MethodType(lambda self, x: x+1, 1)

# Types can be subclasses of other types.
class A(type):
    pass

class B(A):
    pass

issubclass(B, A)

# Types can also be instances of other types.
# This is not a particularly useful thing to do,
# but it is possible.
class C(type):
    pass

C()

# Types can be created dynamically using the 'type' builtin.
# type(name, bases, namespace)
# name: the name of the class to be created
# bases: a tuple of classes that will be used as the base classes
# namespace: a dictionary of attributes that will be added to the class

# The 'type' builtin is also the type of classes.
# This is why we can do things like:
class D(type):
    pass

# This is equivalent to:
type('D', (type,), {})

# We can also dynamically create classes using the 'type' builtin.
# This is a bit like eval, but it is much more flexible
