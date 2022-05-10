from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', '<')
s.size

class Struct(object):
    _fields_ = [('i', '<i')]
Struct.size

class Struct(object):
    _fields_ = [('i', '<i')]
    def __init__(self, *args):
        for name, _, fmt in self._fields_:
            setattr(self, name, args[0])

s = Struct(42)
s.i

class Struct(object):
    _fields_ = [('i', '<i')]
    def __init__(self, *args):
        for name, _, fmt in self._fields_:
            setattr(self, name, args[0])
    def __len__(self):
        return struct.calcsize('<i')

s = Struct(42)
len(s)

class Struct(object):
    _fields_ = [('i', '<i')]
