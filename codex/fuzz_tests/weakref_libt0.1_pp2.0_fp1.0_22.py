import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

class _App(_core.Object):
    """
    The application object.

    This is the main object used to interact with the GUI toolkit. You
    should create only one instance of this class.

    :param str title: The title of the application.
    :param int width: The width of the application window.
    :param int height: The height of the application window.
    :param bool show: Whether to show the application window.
    """
    def __init__(self, title, width, height, show=True):
        super().__init__()
        self._title = title
        self._width = width
        self._height = height
        self._show = show
        self._windows = []
        self._windows_by_id = {}
        self._windows_by_title = {}
        self._windows_by_name = {}
        self._windows_by_ref = weakref.WeakValueDictionary()
        self._windows_by_widget = weakref
