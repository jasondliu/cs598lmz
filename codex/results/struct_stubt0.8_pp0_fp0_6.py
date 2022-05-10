from _struct import Struct
s = Struct.__new__(Struct)
s.alignment = 1
s.size = 1
s

# создать структуру по примеру с помощью .unpack()
def _unpickle_Struct(data):
    return s.unpack(data)

# переопределить возвращаемое значение для метода класса
Struct._unpickle_Struct = _unpickle_Struct

# создать структуру по примеру с помощью .unpack()
s.unpack_from(b'\x00')

import _struct
_struct.Struct('c')
