import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The main application object.

    This object is the main entry point for all GUI applications. It is
    responsible for managing the event loop and dispatching events to the
    appropriate widgets.

    The application object is a singleton, so there can only be one
    application object per process.

    """

    def __init__(self):
        """
        Create a new application object.

        This method should not be called directly. Instead, use the
        :py:func:`start` function.

        """
        super(App, self).__init__()
        self._impl = None
        self._impl_widget = None
        self._impl_window = None
        self._impl_event_loop = None
        self._impl_event_loop_widget = None
        self._impl_event_loop_window = None
        self._impl_event_loop_timer = None
        self._impl
