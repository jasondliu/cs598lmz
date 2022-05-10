from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called without an instance of the class.
# It is called before __init__() and is used to return a new instance of the class.
# The __new__() method is called with the class of the object to be created as its first argument.
# The remaining arguments are those passed to the object constructor expression (the call to the class).
# The return value of __new__() should be the new object instance (usually an instance of cls).
# If __new__() returns an instance of a superclass of cls, then the new instance’s __init__() method will not be invoked.
# If __new__() does not return an instance of cls, then the new instance’s __init__() method will not be invoked,
# and the class’s __init__() method will be called with the new instance as its first argument.
# If __new__() returns an instance of cls, then the new instance’s __init__() method will be invoked like __init__(self,
