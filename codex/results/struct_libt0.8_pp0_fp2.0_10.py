import _struct
from cStringIO import StringIO
from itertools import izip
from struct import pack, unpack

from pygame2.compat import byteify


class Reader(object):
    def __init__(self, stream):
        self._stream = stream

    def __iter__(self):
        return self

    def next(self):
        if not self._stream:
            raise StopIteration
        value = self._stream.read(self.size)
        if len(value) != self.size:
            raise StopIteration
        return self.decode(value)

    def __getitem__(self, index):
        if not isinstance(index, (int, long)):
            raise TypeError("index must be an integer, not %s" % type_name(index))

        self._stream.seek(index * self.size)
        data = self._stream.read(self.size)
        if len(data) != self.size:
            raise IndexError("index out of bounds")
        return self.decode(data)

    def decode(self
