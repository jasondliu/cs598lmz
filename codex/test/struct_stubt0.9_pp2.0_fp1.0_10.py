from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__['format'] = 'I 5s f'
s.__dict__['size'] = calcsize(s.format)
