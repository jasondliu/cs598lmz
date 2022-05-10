import _struct

from . import _common
from . import _exceptions
from . import _util

class _Base(object):
    """
    Base class for all types.
    """

    _size = 0
    _pack_ = None
    _unpack_ = None
    _struct_ = None

    def __init__(self, value=None):
        if value is None:
            value = self._default
        self._value = value

    def __repr__(self):
        return '<{0} {1}>'.format(self.__class__.__name__, self._value)

    def __str__(self):
        return str(self._value)

    def __int__(self):
        return int(self._value)

    def __float__(self):
        return float(self._value)

    def __eq__(self, other):
        return self._value == other

    def __ne__(self, other):
        return self._value != other

    def __lt__(self, other):
        return self._value < other


