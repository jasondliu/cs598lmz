from _struct import Struct
s = Struct.__new__(Struct)
x1.__setattr__('__dict__', {'_endian_':'<', '_fmt_':b'H'})
s._endian_.__setattr__('__dict__', {'_endian_':'<'})
x1._endian_ = s
s = Struct.__new__(Struct)
x1.__setattr__('__dict__', {'_endian_':'<', '_fmt_':b'HI'})
s._endian_.__setattr__('__dict__', {'_endian_':'<'})
s._endian_.__setattr__('__dict__', {'_endian_':x1})
x1._endian_ = s
