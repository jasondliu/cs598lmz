from _struct import Struct
s = Struct.__new__(Struct)
print(s)
print(Struct)
s.__init__("i",)
s.pack(0xffffffff, )
print("pack ", s)
print("unpack ", s.unpack(s.pack(0xffffffff, )))

from abc import ABCMeta, abstractmethod

try:
    import fractions
    import decimal
    import numbers
    import types
    import collections

    class Number(metaclass=ABCMeta):
        __slots__ = ()

        @abstractmethod
        def __int__(self):
            pass

        def __index__(self):
            return self.__int__()

        @classmethod
        def __subclasshook__(cls, C):
            if cls is Number:
                if (any("__int__" in B.__dict__ for B in C.__mro__) and 
                    any("__index__" in B.__dict__ for B in C.__mro__)):
                    return True
            return NotImplemented
except ImportError:
    print("types", types)

