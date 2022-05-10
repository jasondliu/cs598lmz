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
    creating the main window and for running the application.
    """

    def __init__(self, title=None, size=None, position=None,
                 style=None, fullscreen=False, resizable=False,
                 vsync=True, visible=True):
        """
        Create a new application.

        :Parameters:
            `title` : str
                The title of the application.
            `size` : (int, int)
                The size of the application window.
            `position` : (int, int)
                The position of the application window.
            `style` : str
                The style of the application window.
            `fullscreen` : bool
                Whether the application window is fullscreen.
            `resizable` : bool
                Whether the application window is resizable.
            `
