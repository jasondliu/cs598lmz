from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<2s2s2s2s'
s.size = 8
s.pack('a', 'b', 'c', 'd')

# __new__() is a static method, so it is called without an instance of the class.
# It is called before __init__() and is used to return a new instance of the class.
# The __new__() method is called with the class of which an instance was requested as its first argument.
# The remaining arguments are those passed to the object constructor expression.
# If __new__() does not return an instance of cls, then the new instance’s __init__() method will not be invoked.
# __new__() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation.
# It is also commonly overridden in custom metaclasses in order to customize class creation.

# __init__() is a method that is called after the instance has been created (by __new__()),
# but before it is returned to the caller.
# The arguments are those passed to the class constructor expression.

