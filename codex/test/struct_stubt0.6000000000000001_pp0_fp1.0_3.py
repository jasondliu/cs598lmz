from _struct import Struct
s = Struct.__new__(Struct)
s

s.format = 'i'
s.size = s.__sizeof__()
print(s.size)

# class Struct(format, *, source=None):
#     pass

# class Struct(format, *, source=None):
#     def __init__(self, format, *, source=None):
#         pass

# class Struct(format, *, source=None):
#     def __init__(self, format, *, source=None):
#         self.format = format
#         self.size = self.__sizeof__()

# class Struct(format, *, source=None):
#     def __init__(self, format, *, source=None):
#         self.format = format
#         self.size = self.__sizeof__()

# class Struct(format, *, source=None):
#     def __init__(self, format, *, source=None):
#         self.format = format
#         self.size = self.__sizeof__()

# class Struct(format, *
