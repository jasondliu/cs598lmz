from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method (special-cased so you needn't use @staticmethod)
# that takes the class of which an instance was requested as its first argument.
# The remaining arguments are those passed to the object constructor expression
# (the call to the class). The return value of __new__() should be the new object
# instance (usually an instance of cls).

# __init__() is a plain instance method. Its first argument is the new object
# instance, and the remaining arguments are those passed to the object constructor
# expression. If a base class has an __init__() method, the derived class's
# __init__() method, if any, must explicitly call it to ensure proper
# initialization of the base class part of the instance; for example:

class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')

