import gc, weakref

from ..converter import Converter
from ..util import get_object_from_address


class WeakRefConverter(Converter):
    def __init__(self, **kwargs):
        super(WeakRefConverter, self).__init__(**kwargs)
        self.__weakrefs = weakref.WeakSet()

    def _is_valid(self, obj):
        return isinstance(obj, weakref.ref)

    def to_wire(self, obj):
        # weakref.ref(obj)
        assert self._is_valid(obj)
        return obj.__hash__()

    def from_wire(self, obj):
        # weakref.ref(obj)
        assert self._is_valid(obj)
        return obj

    def from_object(self, obj):
        # weakref.ref(obj)
        return weakref.ref(obj)

    def from_memory(self, obj):
        # weakref.ref(obj)
        return weakref.ref(get_object_from_address(obj))
