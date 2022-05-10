import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The main application object.

    This object is the main entry point for all GUI applications. It
    manages the event loop, the main window, and the application
    settings.

    The application object is a singleton, so you can access it from
    anywhere in your application.

    """

    def __init__(self):
        """
        Create a new application object.

        This is a private constructor. You should use the
        :meth:`get_running_app` method to get the singleton instance.

        """
        super(App, self).__init__()
        self._windows = []
        self._main_window = None
        self._title = ''
        self._icon = None
        self._icon_size = None
        self._icon_path = None
        self._icon_file = None
        self._icon_data = None
        self._icon_data_size
