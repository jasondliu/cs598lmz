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
    creating the main window and handling the main loop.

    :param title: The title of the application.
    :param size: The size of the application window.
    :param position: The position of the application window.
    :param fullscreen: Whether the application should be fullscreen.
    :param resizable: Whether the application window should be resizable.
    :param style: The style of the application window.
    :param vsync: Whether the application should use vsync.
    :param visible: Whether the application window should be visible.
    :param icon: The icon of the application window.
    :param min_size: The minimum size of the application window.
    :param max_size: The maximum size of the application window.
    :param cursor: The cursor of the application window.
    :param background_color
