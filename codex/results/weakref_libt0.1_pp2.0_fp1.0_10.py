import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The App class represents the application itself.

    It is used to create windows, and to run the application.
    """

    def __init__(self, title=None, size=None, resizable=False,
                 style=None, fullscreen=False, visible=True,
                 vsync=True, app_name=None, app_id=None,
                 window_class=None):
        """
        Create a new App.

        :Parameters:
            `title` : str
                The title of the window.
            `size` : (int, int)
                The size of the window.
            `resizable` : bool
                Whether the window is resizable.
            `style` : str
                The window style.
            `fullscreen` : bool
                Whether the window is fullscreen.
            `visible` : bool
                Whether the window is visible.
            `vsync`
