import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The App class represents a single application.

    An application is a singleton object that is created when the first
    window is created.

    The App object is used to create windows, and to run the application
    event loop.
    """

    def __init__(self):
        super().__init__()
        self._windows = []

    def run(self):
        """
        Run the application event loop.

        This function will not return until all windows have been closed.
        """
        _core.run()

    def quit(self):
        """
        Quit the application.

        This function will close all windows and exit the application.
        """
        _core.quit()

    def create_window(self, title=None, width=None, height=None):
        """
        Create a new window.

        Args:
            title (str): The title of the window.

