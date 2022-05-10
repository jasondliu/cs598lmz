import weakref

from . import _core
from . import _util
from . import _widget
from . import _window


class _Base(object):
    """Base class for all UI elements.

    The base class is not meant to be used directly.
    """

    def __init__(self):
        self._impl = None
        self._parent = None
        self._children = []

    def _set_parent(self, parent):
        if self._parent is not None:
            self._parent._children.remove(self)
        self._parent = parent
        if parent is not None:
            parent._children.append(self)

    def _set_impl(self, impl):
        if self._impl is not None:
            self._impl.destroy()
        self._impl = impl
        self._impl._set_widget(self)

    def _get_impl(self):
        return self._impl

    def _get_parent(self):
        return self._parent

    def _get_children(self):
        return self._children

    def _get_app(self):
