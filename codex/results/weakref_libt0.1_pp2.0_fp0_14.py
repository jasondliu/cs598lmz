import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['Application']


class Application(_core.Application):
    """
    Application class.

    This class is a wrapper around the native application class.
    """

    def __init__(self, name=None, title=None, icon=None,
                 width=None, height=None, left=None, top=None,
                 resizable=None, style=None, fullscreen=None,
                 visible=None, config=None, **kwargs):
        """
        Create a new application.

        :param name: (str) The name of the application.
        :param title: (str) The title of the application.
        :param icon: (str) The path to the icon of the application.
        :param width: (int) The width of the application.
        :param height: (int) The height of the application.
        :param left: (int) The left position of the application.
        :param top: (int) The top position of the application
