import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The App class represents a single application.

    An application is a singleton object that represents the application
    as a whole. It is used to create windows, and to manage the event
    loop.

    The App class is a subclass of Object, and so inherits all of the
    methods of that class.
    """

    def __init__(self, *args, **kwargs):
        """
        Create a new App object.

        The App class is a singleton, and so this method should not be
        called directly. Instead, use the get_running_app() method to
        retrieve the current application.
        """
        super(App, self).__init__(*args, **kwargs)

        self._windows = []
        self._windows_by_id = {}

        self._event_loop = None

        self._event_loop_thread = None
        self._event_loop_thread
