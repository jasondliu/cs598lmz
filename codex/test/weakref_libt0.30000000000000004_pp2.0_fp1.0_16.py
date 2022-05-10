import weakref

from . import _pyqt5
from . import _pyqt4
from . import _pyside

_backend = None

#------------------------------------------------------------------------------
# Backend
#------------------------------------------------------------------------------

class Backend(object):
    """
    Backend is a singleton class which provides a consistent interface to the
    Qt bindings.
    """
    def __new__(cls, *args, **kwargs):
        global _backend
        if _backend is None:
            _backend = super(Backend, cls).__new__(cls, *args, **kwargs)
        return _backend

    def __init__(self):
        self._qt_api = None
        self._qt_lib = None
        self._qt_version = None
        self._qt_version_str = None
        self._qt_api_version = None
        self._qt_api_version_str = None
        self._qt_bindings_version = None
        self._qt_bindings_version_str = None
