from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called without an instance of the class.
# It is called before __init__() and is used to return a new instance of the class.
# The __new__() method is called after the class has been defined.
# The __init__() method is called after the instance has been created.
# The __new__() method is called before __init__().
# The __new__() method is called with the class as the first argument.
# The __init__() method is called with the instance as the first argument.
# The __new__() method is responsible for returning a new instance of the class.
# The __init__() method is responsible for initializing the instance.
# The __new__() method can be overridden in a subclass to customize instance creation.
# The __init__() method can be overridden in a subclass to customize instance initialization.
# The __new__() method is a static method.
# The __init__() method is a non-static method.
# The __new__() method is
