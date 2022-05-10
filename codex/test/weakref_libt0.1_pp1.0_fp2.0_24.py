import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The App class represents a running application.

    An application is a singleton object that is created when the application
    starts.

    The App class provides access to the application's main window, and
    provides methods for running the application.
    """

    def __init__(self):
        """
        Create a new App object.
        """
        super(App, self).__init__()

        self._main_window = None
        self._main_window_ref = None

        self._running = False

    def run(self):
        """
        Run the application.

        This method starts the application's main event loop. It will not
        return until the application is closed.
        """
        if self._running:
            raise RuntimeError('Application is already running')

        self._running = True
        _core.run_app(self)

