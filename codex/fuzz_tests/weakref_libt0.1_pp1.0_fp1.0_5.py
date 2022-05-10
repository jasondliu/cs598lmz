import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

class _App(_core.Object):
    """
    The application object.

    This is the main object used to interact with the GUI toolkit.
    It is used to create windows and widgets, and to run the main
    event loop.
    """

    def __init__(self):
        """
        Create a new application object.
        """
        super().__init__()
        self._windows = []
        self._windows_by_id = {}
        self._windows_by_handle = {}
        self._windows_by_widget = {}
        self._windows_by_widget_handle = {}
        self._windows_by_widget_id = {}
        self._windows_by_widget_handle_id = {}
        self._windows_by_widget_handle_id_handle = {}
        self._windows_by_widget_handle_id_handle_id = {}
        self._windows_by_widget_handle_id_handle_id_handle = {}
       
