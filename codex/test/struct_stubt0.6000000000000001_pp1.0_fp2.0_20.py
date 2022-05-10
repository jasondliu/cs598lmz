from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format', 'I 2s f')
s.__setattr__('size', 16)
s.__setattr__('_u', 'I 2s f')
s.__setattr__('_fmt', '=I 2s f')
