from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it can be called on the class, not an instance.
# It is called before __init__() and is passed the class of which an instance was requested as its first argument.
# The remaining arguments are those passed to the class constructor expression.
# The return value of __new__() should be the new object instance (usually an instance of cls).

# __init__() is a regular instance method.
# It is called after the instance has been created (by __new__()), but before it is returned to the caller.
# The arguments are those passed to the class constructor expression.
# If a base class has an __init__() method, the derived class’s __init__() method, if any, must explicitly call it to ensure proper initialization of the base class part of the instance;
# for example:

class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        Base.__init__(self
