import gc, weakref

from . import _ext

class PackedTuple(tuple):
    """
    A tuple subclass that uses a packed array.
    """
    def __new__(cls, *items):
        items = tuple(items)
        return super(PackedTuple, cls).__new__(cls, items)

    def __init__(self, *items):
        self._array = _ext.PackedArray.from_sequence(self)

    @property
    def array(self):
        return self._array

class PackedArray(object):
    """
    A packed array that is a subclass of :class:`tuple`.
    """
    def __init__(self, *items):
        self._array = _ext.PackedArray.from_sequence(items)

    def __getitem__(self, index):
        return self._array[index]

    def __len__(self):
        return self._array.size

    @property
    def array(self):
        return self._array

class PackedArrayBuffer(object):

