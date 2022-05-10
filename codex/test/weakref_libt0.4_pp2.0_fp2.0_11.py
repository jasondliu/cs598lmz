import weakref

from . import _core

class _Mock(_core.Mock):
    def __init__(self, name, parent, return_value, side_effect,
                 unsafe=False):
        self._parent = weakref.ref(parent) if parent is not None else None
        self._unsafe = unsafe
        super(_Mock, self).__init__(name, return_value, side_effect)

    def _get_parent(self):
        if self._parent is None:
            return None
        return self._parent()

    def _set_parent(self, parent):
        self._parent = weakref.ref(parent) if parent is not None else None

    parent = property(_get_parent, _set_parent)

    def _get_unsafe(self):
        return self._unsafe

    def _set_unsafe(self, unsafe):
        self._unsafe = unsafe

    unsafe = property(_get_unsafe, _set_unsafe)

