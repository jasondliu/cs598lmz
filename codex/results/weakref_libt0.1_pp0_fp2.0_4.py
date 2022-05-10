import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['Application']


class Application(_core.Application):
    """
    Application class.

    This class is the main entry point for the application.
    """

    def __init__(self, title=None, width=None, height=None,
                 left=None, top=None, right=None, bottom=None,
                 fullscreen=False, resizable=False,
                 style=None, visible=True, **kwargs):
        """
        Create a new application.

        Args:
            title (str): The title of the application.
            width (int): The width of the application.
            height (int): The height of the application.
            left (int): The left position of the application.
            top (int): The top position of the application.
            right (int): The right position of the application.
            bottom (int): The bottom position of the application.
            fullscreen (bool): Whether the application is fullscreen.
            resizable (bool
