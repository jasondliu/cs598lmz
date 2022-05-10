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
    starts. It is used to create windows and to handle events.

    The App class is a subclass of Object, and inherits all of the methods
    and properties of that class.
    """

    def __init__(self, *args, **kwargs):
        """
        Create a new App object.

        The App object is a singleton, so this method should not be called
        directly. Instead, use the :py:func:`~flexx.app.App.instance` method
        to get the singleton instance.
        """
        super().__init__(*args, **kwargs)

        self._windows = []
        self._windows_by_id = {}
        self._windows_by_title = {}

        self._next_window_id = 1

        self._timer
