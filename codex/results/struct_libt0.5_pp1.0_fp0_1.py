import _struct

class Struct(object):
    def __init__(self, *args):
        self._struct = _struct.Struct(*args)
        self._format = self._struct.format
        self._size = self._struct.size

    def pack(self, *args):
        return self._struct.pack(*args)

    def unpack(self, *args):
        return self._struct.unpack(*args)

    @property
    def format(self):
        return self._format

    @property
    def size(self):
        return self._size
