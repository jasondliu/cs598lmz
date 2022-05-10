import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['App']


class App(_core.Object):
    """
    The App class represents the application.

    It is used to create the main window and to start the main event loop.
    """

    def __init__(self, title=None, width=None, height=None,
                 left=None, top=None, right=None, bottom=None,
                 border=None, border_left=None, border_top=None,
                 border_right=None, border_bottom=None,
                 on_close=None, on_key_down=None, on_key_up=None,
                 on_mouse_down=None, on_mouse_up=None, on_mouse_move=None,
                 on_mouse_wheel=None, on_mouse_enter=None,
                 on_mouse_leave=None, on_resize=None, on_show=None,
                 on_hide=None, on_move=None, on_focus
