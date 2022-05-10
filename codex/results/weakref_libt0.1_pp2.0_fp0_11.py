import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['Application']


class Application(_core.Application):
    """
    Application class.

    This class is the main entry point for creating a GUI application.
    """

    def __init__(self, title=None, size=None, position=None,
                 style=None, fullscreen=False, resizable=False,
                 vsync=True, visible=True, **kwargs):
        """
        Create a new application.

        Parameters
        ----------
        title : str, optional
            The title of the application.
        size : (int, int), optional
            The size of the application.
        position : (int, int), optional
            The position of the application.
        style : str, optional
            The style of the application.
        fullscreen : bool, optional
            Whether the application should be fullscreen.
        resizable : bool, optional
            Whether the application should be resizable.
        vsync : bool, optional
            Whether the application should use
