import types
types.MethodType(lambda self, x: x + 1, None)

# MethodType is a callable that binds a function to an instance of a class
# this is how methods are implemented in python

# the first argument is the function, the second is the instance to bind it to
# the instance is stored in the __self__ attribute of the function

# the instance does not have to be an instance of the class the function is defined in
# but if it is not, the function may not work correctly, depending on its implementation

# the __get__ method of a function object is used to implement the binding
# this is called when a function is accessed as an attribute of an instance
# the function is returned unchanged if there is no instance, or if the instance is None
# otherwise, a MethodType instance is returned, with the function and instance

# since the __get__ method is used for attribute access, a function can be used as a class attribute
# and will only be bound to instances of that class

# the __get__ method of a function can be replaced to customize the way it is bound
# this is called a "descriptor"
#
