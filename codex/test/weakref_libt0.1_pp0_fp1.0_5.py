import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['Application']


class Application(_core.Application):
    """
    The application object.

    This is the main object of the application. It is responsible for
    managing the event loop and the main window.

    The application object is a singleton, so you can't create more than
    one instance. Use the :meth:`get_application` method to get the
    application object.

    """

    def __init__(self):
        super().__init__()
        self._windows = weakref.WeakSet()

    def run(self):
        """
        Run the application.

        This method starts the event loop. It will return when the last
        window is closed.

        """
        self._run()

    def quit(self):
        """
        Quit the application.

        This method quits the application. It will close all windows and
        stop the event loop.

        """
        self._quit()

