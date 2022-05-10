from _struct import Struct
s = Struct.__new__(Struct); s._fields_ = [('name', 's'),('sh_name', 'H'),('type', 'I'),('flags', 'I'),('addr', 'Q'),('offset', 'Q'),('size', 'Q'),('link', 'I'),('info', 'I'),('align', 'Q'),('entsize', 'Q'),('elements', object)]
class Sym(Structure):
    __slots__ = ('_',)
    _values = { 'desc':{ 'BIND_WEAK':1, 'BIND_GLOBAL':0, 'BIND_LOCAL':1025, 'BIND_EXTERN':2, 'TYPE_FUNC':0x20, 'TYPE_SECTION':0x40, 'BIND_LABEL':4 }, 'type':{ 'SHT_PROGBITS':1, 'SHT_NOBITS':8, 'SHT_NULL':0, 'SHT_RELA':3, 'SHT_DYNSYM':11 }, 'other':{ 'STV_DEFAULT':0, 'STV_HIDDEN':2, 'STB
