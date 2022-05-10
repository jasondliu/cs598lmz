import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The App class represents the application itself.
    """

    def __init__(self, *args, **kwargs):
        """
        Create a new App object.
        """
        super(App, self).__init__(*args, **kwargs)
        self._windows = []
        self._windows_by_id = {}
        self._windows_by_handle = {}
        self._windows_by_name = {}
        self._windows_by_title = {}
        self._windows_by_class = {}
        self._windows_by_process = {}
        self._windows_by_thread = {}
