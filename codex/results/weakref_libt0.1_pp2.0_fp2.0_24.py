import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App', 'AppError']


class AppError(Exception):
    pass


class App(_core.Core):
    """
    The main application class.

    This class is used to create the main application window and to
    start the application event loop.

    :param title: The title of the application window.
    :param size: The size of the application window.
    :param position: The position of the application window.
    :param style: The style of the application window.
    :param fullscreen: Whether the application window should be fullscreen.
    :param resizable: Whether the application window should be resizable.
    :param no_frame: Whether the application window should have a frame.
    :param visible: Whether the application window should be visible.
    :param vsync: Whether the application window should use vsync.
    :param min_size: The minimum size of the application window.
    :param max_size: The maximum size of the application window.
   
