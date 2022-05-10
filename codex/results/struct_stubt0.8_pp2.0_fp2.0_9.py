from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda: 1

print(s.size())  # prints 1
