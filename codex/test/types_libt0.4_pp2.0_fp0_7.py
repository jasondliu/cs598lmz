import types
types.MethodType(f, None, None)

# MethodType(function, instance, class)

# Method types are used to implement bound and unbound methods.
# Unbound methods are functions that are stored in a class as a class attribute.
# They are not bound to an instance of the class, but they can be called on an instance.
# Bound methods are methods that are called on an instance of a class.
# They are stored as instance attributes and are bound to the instance.

# An unbound method can be called on an instance of its class.
# The instance becomes the first argument of the function.

# An unbound method can also be called on a class.
# The class becomes the first argument of the function.

# A bound method can be called on an instance of its class.
# The instance is passed to the function as the first argument automatically.

# A bound method cannot be called on a class.
# An unbound method can be converted to a bound method using the instance method.
# An unbound method can be converted to a bound method using the class method.

# An unbound method can be converted to a
