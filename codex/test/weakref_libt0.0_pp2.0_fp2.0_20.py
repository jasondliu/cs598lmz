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

        This method will block until the application is closed.
        """
