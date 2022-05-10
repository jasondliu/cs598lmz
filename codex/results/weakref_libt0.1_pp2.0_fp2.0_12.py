import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The App class represents a single application.

    An application is a singleton object that is created when the application
    starts. It is used to create windows, and to run the application's event
    loop.

    The App class is a subclass of Object, and inherits all of the methods
    and properties of that class.
    """

    def __init__(self):
        """
        Creates a new App object.

        This method should not be called directly. Instead, use the
        :func:`~flexx.app.App.instance` method to get the singleton instance.
        """
        super().__init__()

        self._windows = []
        self._windows_by_id = {}
        self._windows_by_title = {}

        self._timer = None
        self._timer_interval = 0.0
        self._timer_callback = None

        self._event_
