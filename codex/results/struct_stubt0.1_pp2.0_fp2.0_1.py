from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called without an instance of the class.
# It is called before __init__() and is responsible for returning a new instance of your class.
# In the example above, __new__() is called on the class, Struct, and returns an instance of Struct.
# In this case, the class instance is created by the __new__() method of the superclass, Struct.
# The __init__() method is then called on the new instance, with the arguments that were passed to __new__().

# The __new__() method is intended mainly to allow subclasses of immutable types (like int, str, or tuple)
# to customize instance creation. It is also commonly overridden in custom metaclasses in order to customize class creation.

# __new__() is, in most cases, the right place to put code that modifies the arguments passed to the class constructor.
# If you only need to modify the instance after it has been created, then you should use __init__() instead.

# __new__() is a static
