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
        """
        Create a new App object.
        """
        super(App, self).__init__(*args, **kwargs)
        self._windows = []

    def run(self):
        """
        Run the application.
        """
        self._run()

    def quit(self):
        """
        Quit the application.
        """
        self._quit()

    def add_window(self, window):
        """
        Add a window to the application.
        """
        self._windows.append(weakref.ref(window))
