import weakref

from . import _lib


class _PyObjectWrapper(_lib.PyObject):
    """
    Wrapper for C-level PyObjects.
    """
    __slots__ = ('_weakref', '_weakref_callback')
    _weakref = None
    _weakref_callback = None

    def __init__(self, *args, **kwargs):
        super(_PyObjectWrapper, self).__init__(*args, **kwargs)
        self._weakref = weakref.ref(self, self._weakref_callback)

    def _weakref_callback(self, _):
        self._weakref = None
        _lib.Py_DecRef(self)

    def __del__(self):
        if self._weakref is not None:
            self._weakref()


class _PyObjectWrapperWithFinalizer(_PyObjectWrapper):
    """
    Wrapper for C-level PyObjects that have a finalizer.
    """
    __slots__ = ()
