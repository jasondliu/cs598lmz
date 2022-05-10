import _struct

class Struct(object):
    '''
    create a struct object from a list and a format
    '''
    def __init__(self, format, fields):
        self._fmt = format
        self._packed = _struct.pack(self._fmt, *fields)
        self._unpacked = _struct.unpack(self._fmt, self._packed)

    def __len__(self):
        return _struct.calcsize(self._fmt)

    def __getitem__(self, i):
        return self._unpacked[i]

    def __iter__(self):
        return iter(self._unpacked)

    def __str__(self):
        return self._fmt + ': ' + ', '.join(str(s) for s in self._unpacked)

    def __repr__(self):
        return 'Struct(%r, %r)' % (self._fmt, list(self))

    def __add__(self, other):
        return Struct(self._fmt + other._fmt, list(self) +
