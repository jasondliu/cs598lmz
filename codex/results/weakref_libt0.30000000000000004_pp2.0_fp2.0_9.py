import weakref

from . import _core
from . import _util
from . import _widget

__all__ = ['View']


class View(_widget.Widget):
    """
    A widget that displays a :class:`~kivy.graphics.Canvas`.

    The :class:`View` widget is a widget that displays a
    :class:`~kivy.graphics.Canvas`. It is the most basic widget that can be
    used to display graphics.

    The :class:`View` widget is a widget that displays a
    :class:`~kivy.graphics.Canvas`. It is the most basic widget that can be
    used to display graphics.

    .. versionchanged:: 1.10.0

        The :class:`View` widget is now a :class:`~kivy.uix.widget.Widget`
        instead of a :class:`~kivy.uix.scatter.Scatter`.

    .. versionchanged:: 1.9.0

        The :class:`View` widget is now a :class:`~kivy
