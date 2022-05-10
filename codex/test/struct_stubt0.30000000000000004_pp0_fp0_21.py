from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a class method, so it is called on the class, not an instance.
# It is called before __init__, and is responsible for returning a new instance of the class.
# It is possible to override __new__ to customize the creation of a new instance.
# __new__ is called with the class of the instance as the first argument,
# and the arguments that would be passed to __init__ as the rest of the arguments.
# The return value of __new__ must be an instance of the class.
# If you want to customize the creation of an instance, you can override __new__.
# If you want to customize the initialization of an instance, you can override __init__.
# If you want to customize both, you can override __new__ and call __init__ from it.

# __new__ is called before __init__.
# The return value of __new__ is passed to __init__.
# If __new__ returns an instance of cls, then the new instance’s __init__ method will be invoked like __init__
