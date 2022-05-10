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

        :param args: Positional arguments to pass to the superclass.
        :param kwargs: Keyword arguments to pass to the superclass.
        """
        super(App, self).__init__(*args, **kwargs)

        self._windows = []

    def run(self):
        """
        Run the application.

        This method will not return until the application is closed.
        """
