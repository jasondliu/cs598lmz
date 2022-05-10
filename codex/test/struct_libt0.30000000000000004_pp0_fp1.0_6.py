import _struct

#
#
#

class _Base(object):

    def __init__(self, fmt, data):
        self._fmt = fmt
        self._data = data

    def __str__(self):
        return self._fmt % self._data

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, _Base):
            return self._data == other._data
        return self._data == other

    def __ne__(self, other):
        if isinstance(other, _Base):
            return self._data != other._data
        return self._data != other

    def __lt__(self, other):
        if isinstance(other, _Base):
            return self._data < other._data
        return self._data < other

    def __le__(self, other):
        if isinstance(other, _Base):
            return self._data <= other._data
        return self._data <= other

