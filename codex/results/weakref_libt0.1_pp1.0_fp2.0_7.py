import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['Application']


class Application(_core.Application):
    """
    Application class.

    This class is the main class of the application.
    """

    def __init__(self, title='', width=640, height=480, **kwargs):
        """
        Initialize the application.

        :param title: The title of the application.
        :param width: The width of the application window.
        :param height: The height of the application window.
        :param kwargs: The keyword arguments passed to the super class.
        """
        super().__init__(title, width, height, **kwargs)
        self._windows = weakref.WeakSet()

    def run(self):
        """
        Run the application.

        This method will start the main loop of the application.
        """
        self._running = True
        while self._running:
            self._update()
            self._draw()
            self._swap_buffers
