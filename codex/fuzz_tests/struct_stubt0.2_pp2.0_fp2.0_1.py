from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a class method, so it is called on the class, not on an instance.
# It is called before __init__() and is passed the class itself as the first argument.
# It is also passed any arguments passed to the class constructor expression.
# The return value of __new__() is passed to __init__() as the first argument.
# If __new__() returns an instance of cls, then the new instance’s __init__() method will be invoked like __init__(self[, ...]),
# where self is the new instance and the remaining arguments are the same as were passed to __new__().
# If __new__() does not return an instance of cls, then the new instance’s __init__() method will not be invoked.
# __new__() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation.
# It is also commonly overridden in custom metaclasses in order to customize class creation.
# __new__() is, in general, a low-
