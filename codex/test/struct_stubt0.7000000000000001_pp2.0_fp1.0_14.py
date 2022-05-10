from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'HH'
s.size = s.calcsize(s.format)


class Record(object):

    def __init__(self, data, offset, parent):
        self._data = data
        self._offset = offset
        self._parent = parent

        self.tag, self.size = s.unpack_from(data, offset)

    def __repr__(self):
        return ('<%s: tag=%d, size=%d>'
                % (self.__class__.__name__, self.tag, self.size))

    def _unpack(self, fmt):
        return s.unpack(fmt, self._data, self._offset + s.size)

    def _unpack_one(self, fmt):
        return self._unpack(fmt)[0]

    def _get_offset(self, offset, fmt):
        return offset + self._unpack_one(fmt) * 2
