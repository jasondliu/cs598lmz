import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

class _App(_core.Object):
    """
    The application object.
    
    This is the main object of the library. It is used to create windows,
    and to run the main loop.
    """
    def __init__(self):
        super().__init__()
        self._windows = []
        self._windows_by_id = {}
        self._windows_by_handle = {}
        self._windows_by_name = {}
        self._windows_by_title = {}
        self._windows_by_class = {}
        self._windows_by_pid = {}
        self._windows_by_hwnd = {}
        self._windows_by_hwnd_parent = {}
        self._windows_by_hwnd_owner = {}
        self._windows_by_hwnd_child = {}
        self._windows_by_hwnd_sibling = {}
        self._windows_by_hwnd_thread = {}
