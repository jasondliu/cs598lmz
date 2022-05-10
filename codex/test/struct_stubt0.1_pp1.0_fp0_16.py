from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called without an instance.
# It is called before __init__()
# It is used to return a new instance of the class.
# It is used to control the creation of a new instance.
# It can be overridden when you need to control the creation of a new instance.
# The __new__() method is similar to the __init__() method, but there are two
# important differences:
# The __new__() method is run before __init__()
# The __new__() method is responsible for returning a new instance of your class
# The __init__() method is responsible for initializing the object
# The __new__() method takes the class of which an instance was requested as its
# first argument.
# The remaining arguments are those passed to the object constructor expression
# The return value of __new__() should be the new object instance (usually an
# instance of cls).
# If __new__() does not return an instance of cls, then the new instance’s
# __init
