from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format', 'I 2s f')
s.size = s.__sizeof__()


print(s.size)
