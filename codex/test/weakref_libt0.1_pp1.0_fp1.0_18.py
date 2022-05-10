import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The App class represents the application itself.
    """

    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self._windows = []

    def run(self):
        """
        Run the application.
        """
        _core.App.run(self)

    def quit(self):
        """
        Quit the application.
        """
        _core.App.quit(self)

    def add_window(self, window):
        """
        Add a window to the application.
        """
        self._windows.append(window)

    def remove_window(self, window):
        """
        Remove a window from the application.
        """
