from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('_fmt', '12s f')
s.__setattr__('size', s.size)
s.__setattr__('pack', s.pack)
s.__setattr__('unpack', s.unpack)
s.__setattr__('format', s.format)
