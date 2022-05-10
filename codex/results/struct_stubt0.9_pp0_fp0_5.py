from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'HH'
s.size = s.calcsize(s.format)
print(s.size)

# s.unpack(b'AB')

# def unpack(self, data):
#     return self.error('cannot decode integer')

# s = Struct.__new__(Struct)
# s.format = 'B'
# s.size = s.calcsize(s.format)
# print(s.size)


# class record(tuple):
#     __slots__ = ()
#     _fields = []

#     def __new__(cls, *args, **kwds):
#         return tuple.__new__(cls, (args, kwds))

#     @classmethod
#     def __prepare__(cls, name, bases):
#         return {}

#     def __init__(self, *args, **kwds):
#         pass

#     def __reduce_ex__(self, proto):
#         return super().__reduce_ex__(
