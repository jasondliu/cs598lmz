from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i').__new__(str)
except TypeError as err:
    print(err)

# __init__ adds attributes and checks name is valid
try:
    s = Struct.__new__(Struct)
    s.__init__('i')
except ValueError as err:
    print(err)

# created instance can be called (__new__ is not called)
s = Struct('i')
s.size

# direct call returns a new instance
s2 = Struct('i')
s is s2

# subclass with kwargs
class SubStruct(Struct):
    def __init__(self, format, verbose=False, **kwargs):
        self.__verbose = verbose
        super().__init__(format, **kwargs)

