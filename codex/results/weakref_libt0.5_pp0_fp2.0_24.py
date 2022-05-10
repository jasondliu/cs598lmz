import weakref

from . import _core
from . import _util

from . import _widgets

class Widget(_core._Widget):
    """
    Base widget class.

    Widgets are the base class for all visible objects on the screen.
    """

    def __init__(self, x=0, y=0, width=0, height=0,
                 style=None, parent=None, **kwargs):
        """
        Create a new widget.

        :Parameters:
            `x` : int
                X coordinate of the widget.
            `y` : int
                Y coordinate of the widget.
            `width` : int
                Width of the widget.
            `height` : int
                Height of the widget.
            `style` : `Style`
                Style to use for this widget. If no style is provided, the
                widget inherits the style of its parent.
            `parent` : `Widget`
                Parent widget.

        The remaining keyword arguments are set as widget attributes on
        construction.
        """
        super(Widget, self).__init__(x, y
