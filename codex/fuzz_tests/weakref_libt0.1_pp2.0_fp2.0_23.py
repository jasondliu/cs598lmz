import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The App class represents a single application.

    An application is a singleton object that is created when the first
    window is created.

    The App class is used to create windows, and to run the application
    event loop.
    """

    def __init__(self):
        super(App, self).__init__()
        self._windows = []
        self._windows_by_id = {}
        self._windows_by_handle = {}
        self._windows_by_name = {}
        self._windows_by_title = {}
        self._windows_by_class = {}
        self._windows_by_pid = {}
        self._windows_by_path = {}
        self._windows_by_control_id = {}
        self._windows_by_control_handle = {}
        self._windows_by_control_name = {}
        self._windows_by_control_
