import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The App class represents the application.

    It is used to create the main window and to start the application.
    """

    def __init__(self, title='', width=640, height=480, resizable=False,
                 style=None, **kwargs):
        """
        Create a new App.

        Args:
            title (str): The title of the window.
            width (int): The width of the window.
            height (int): The height of the window.
            resizable (bool): Whether the window is resizable.
            style (Style): The style of the window.
            **kwargs: Additional keyword arguments are passed to the
                :class:`Window` constructor.
        """
        super().__init__()

        self._window = _window.Window(title, width, height, resizable, style,
                                      **kwargs)
        self._window._
